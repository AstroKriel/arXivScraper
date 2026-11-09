## { U-TEST

##
## === DEPENDENCIES
##

## stdlib
import argparse
import tempfile
import unittest
from pathlib import Path
from unittest import mock

## local
from arxivscraper.support import input_value_types

##
## === TEST SUITE
##


class TestArxivId_Conversion(unittest.TestCase):

    def test_accepts_old_and_new_length_ids(
        self,
    ) -> None:
        convert_fn = input_value_types.InputValueTypes.ARXIV_ID.convert_fn
        self.assertEqual(convert_fn("2310.17036"), "2310.17036")
        self.assertEqual(convert_fn(" 1501.0123 "), "1501.0123")

    def test_rejects_anything_else(
        self,
    ) -> None:
        convert_fn = input_value_types.InputValueTypes.ARXIV_ID.convert_fn
        for bad_text in ["2310.170", "2310-17036", "arXiv:2310.17036", ""]:
            with self.assertRaises(argparse.ArgumentTypeError, msg=bad_text):
                convert_fn(bad_text)


class TestTag_Conversion(unittest.TestCase):

    def test_lowercases_one_word(
        self,
    ) -> None:
        self.assertEqual(input_value_types.InputValueTypes.TAG.convert_fn(" MHD "), "mhd")

    def test_rejects_empty_and_spaced_tags(
        self,
    ) -> None:
        for bad_text in ["", "   ", "mhd test"]:
            with self.assertRaises(argparse.ArgumentTypeError, msg=bad_text):
                input_value_types.InputValueTypes.TAG.convert_fn(bad_text)


class TestProfile_Conversion(unittest.TestCase):

    def setUp(
        self,
    ) -> None:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        project_root = Path(temporary_directory.name)
        search_configs_dir = project_root / "configs" / "search"
        search_configs_dir.mkdir(parents=True)
        (search_configs_dir / "mhd.toml").write_text("")
        (search_configs_dir / "profile.example.toml").write_text("")
        environment_patch = mock.patch.dict("os.environ", {"ARXIVSCRAPER_ROOT": str(project_root)})
        environment_patch.start()
        self.addCleanup(environment_patch.stop)

    def test_accepts_a_profile_with_a_config_file(
        self,
    ) -> None:
        self.assertEqual(input_value_types.InputValueTypes.PROFILE.convert_fn("mhd"), "mhd")

    def test_rejects_a_missing_profile_and_lists_the_ones_there_are(
        self,
    ) -> None:
        with self.assertRaises(argparse.ArgumentTypeError) as error_context:
            input_value_types.InputValueTypes.PROFILE.convert_fn("ism")
        self.assertIn("profiles: mhd.", str(error_context.exception))

    def test_rejects_a_template(
        self,
    ) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            input_value_types.InputValueTypes.PROFILE.convert_fn("profile.example")


##
## === ENTRY POINT
##

if __name__ == "__main__":
    unittest.main()

## } U-TEST
