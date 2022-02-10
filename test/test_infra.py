import pytest
import os

""" use this exaple test later when we can actuslly run the service

"""
home_dir = os.path.expanduser("~")

@pytest.mark.parametrize(
    "command,exit_code",
    [
        ("git --version", 0),
        ("tree --version", 0),
        ("make --version", 0),
        ("curl --version", 0),
        ("zip --version", 0),
        ("unzip --version", 10),
        ("fzf --version", 0),
        ("rg --version", 0),
    ],
)
def test_run_binaries(host, command, exit_code):
    """Try to run  each of binaries we need in the image

    test the exit code for each
    """
    cmd = host.run(command)
    assert cmd.rc == exit_code


@pytest.mark.parametrize(
    "file_name",
    [
        ("add_home_bin_to_path.sh"),
        ("aliases.sh"),
        ("aws_functions.sh"),
        ("bash_powerline.sh"),
        ("git_aliases.sh"),
        ("git_functions.sh"),
        ("ohmyzsh_git_aliases.sh"),
        ("ssh_aliases.sh"),
        ("temp_aliases.sh"),
        ("terragrunt_aliases.sh"),
        ("fzf.sh"),
        ("editor.sh"),
    ],
)
def test_files_exist(host, file_name):
    """Try to run  each of binaries we need in the image

    test the exit code for each
    """

    this_file = host.file(f"{home_dir}/bashrc.d/{file_name}")
    assert this_file.exists
