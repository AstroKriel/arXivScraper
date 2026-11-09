## { U-TEST

##
## === DEPENDENCIES
##

## stdlib
import contextlib
import inspect
import io
import unittest

## personal
from huginn import manage_cli

## local
from arxivscraper import app

##
## === TEST SUITE
##


class TestCommandTable_Signatures(unittest.TestCase):

    def test_every_cmd_fn_takes_exactly_its_args_by_keyword(
        self,
    ) -> None:
        for cmd in app.COMMAND_LINE_TOOL.all_cmds:
            fn_params = inspect.signature(cmd.fn).parameters.values()
            fn_param_names = {_fn_param.name for _fn_param in fn_params}
            arg_param_names = {_arg.param_name for _arg in cmd.args}
            self.assertEqual(fn_param_names, arg_param_names, cmd.name)
            for fn_param in fn_params:
                self.assertIs(fn_param.kind, inspect.Parameter.KEYWORD_ONLY, f"{cmd.name}: {fn_param.name}")


class TestCommandTable_Help(unittest.TestCase):

    def test_help_lists_every_cmd(
        self,
    ) -> None:
        stdout_buffer = io.StringIO()
        with contextlib.redirect_stdout(stdout_buffer):
            manage_cli.run_cli(
                command_line_tool=app.COMMAND_LINE_TOOL,
                argv=["--help"],
            )
        help_text = stdout_buffer.getvalue()
        for cmd in app.COMMAND_LINE_TOOL.all_cmds:
            self.assertIn(f"    {cmd.name} ", help_text)


##
## === ENTRY POINT
##

if __name__ == "__main__":
    unittest.main()

## } U-TEST
