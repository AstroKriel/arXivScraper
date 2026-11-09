## { MODULE

##
## === DEPENDENCIES
##

## personal
from huginn import (
    cmd_args,
    manage_cli,
    manage_log,
)

## local
from arxivscraper.support import input_value_types
from arxivscraper.workflows import (
    ai_score,
    browse_papers,
    download_pdfs,
    fetch_paper,
    retag,
    search_arxiv,
)

##
## === COMMAND TABLE
##

COMMAND_LINE_TOOL = manage_cli.CommandLineTool(
    name="arxivscraper",
    description="find, score, and triage arXiv papers that match your search profiles",
    cmd_groups=[
        manage_cli.CommandGroup(
            title="Finding papers",
            cmds=[
                manage_cli.Command(
                    name="search",
                    description="search arXiv with a search profile and save the new matching papers",
                    fn=search_arxiv.cmd_search,
                    args=[
                        cmd_args.PositionalArgument(
                            param_name="profile_name",
                            description="a search profile in configs/search/, named without .toml; asked for if left out",
                            input_value_type=input_value_types.InputValueTypes.PROFILE,
                            allowed_num_input_values=cmd_args.AllowedNumInputValues.ZERO_OR_ONE,
                        ),
                        cmd_args.NamedArgument(
                            long_arg_name="lookback-days",
                            short_arg_name="lb",
                            description="how many days back to search; asked for if left out",
                            input_value_type=input_value_types.InputValueTypes.NUMBER,
                        ),
                        cmd_args.NamedArgument(
                            long_arg_name="from-date",
                            short_arg_name="fd",
                            description="the last day of the search window (default: today)",
                            input_value_type=input_value_types.InputValueTypes.DATE,
                        ),
                    ],
                ),
                manage_cli.Command(
                    name="fetch",
                    description="save one paper by its arXiv id, after showing it for confirmation",
                    fn=fetch_paper.cmd_fetch,
                    args=[
                        cmd_args.PositionalArgument(
                            param_name="arxiv_id",
                            description="the arXiv id, e.g. 2310.17036; asked for if left out",
                            input_value_type=input_value_types.InputValueTypes.ARXIV_ID,
                            allowed_num_input_values=cmd_args.AllowedNumInputValues.ZERO_OR_ONE,
                        ),
                    ],
                ),
                manage_cli.Command(
                    name="download",
                    description="download the PDF of every paper marked for download",
                    fn=download_pdfs.cmd_download,
                ),
            ],
        ),
        manage_cli.CommandGroup(
            title="Triaging papers",
            cmds=[
                manage_cli.Command(
                    name="score",
                    description="rate every unscored paper with the AI provider in configs/ai/",
                    fn=ai_score.cmd_score,
                    args=[
                        cmd_args.NamedArgument(
                            long_arg_name="model",
                            description="the model to use, instead of the one in ai_provider.toml",
                            input_value_type=input_value_types.InputValueTypes.TEXT,
                        ),
                        cmd_args.NamedArgument(
                            long_arg_name="base-url",
                            description="the API base URL to use, instead of the one in ai_provider.toml",
                            input_value_type=input_value_types.InputValueTypes.TEXT,
                        ),
                    ],
                ),
                manage_cli.Command(
                    name="retag",
                    description="re-check every saved paper against every search profile and update its tags",
                    fn=retag.cmd_retag,
                ),
                manage_cli.Command(
                    name="browse",
                    description="open the paper browser to read abstracts and set each paper's status",
                    fn=browse_papers.cmd_browse,
                ),
            ],
        ),
    ],
)

##
## === ENTRY POINT
##


def main() -> None:
    log_file_path = manage_log.get_home_log_file_path(tool_name=COMMAND_LINE_TOOL.name)
    manage_log.set_log_file_path(log_file_path=log_file_path)
    manage_cli.run_cli(command_line_tool=COMMAND_LINE_TOOL)


## } MODULE
