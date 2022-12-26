import logging
import os
import sys
import subprocess


# suggest use shell script for incremental pep8 check
# find shell script in our organization Shell_Scripting repo
class PythonStyleChecker(object):
    """
    Base class for python style checker.
    Implemented pep8. My include pylint later.
    """

    def __init__(self, checker_name):
        self.passed = 0
        self.failed = 0
        self._checker_name = checker_name

    @property
    def checker_name(self):
        return self._checker_name

    def check_style(self, module):
        raise NotImplementedError


class Pep8Checker(PythonStyleChecker):
    """pep8 style checker"""

    def __init__(self):
        super(Pep8Checker, self).__init__('pep8')

    def check_style(self, module):
        '''Runs pep8 on a Python module.'''
        try:
            subprocess.check_output([self.checker_name, module])
            LOGGER.debug('%s PASSED.', module)
            self.passed += 1
        except subprocess.CalledProcessError as pep8_error:
            pep8_message = pep8_error.output
            LOGGER.warning('%s FAILED PEP8', os.path.relpath(module))
            self.failed += 1
            for pep8_warning in pep8_message.splitlines():
                LOGGER.warning(pep8_warning)


def _get_starting_directory(args):
    try:
        base_directory = args[1]
    except IndexError:
        base_directory = os.getcwd()
    return base_directory


base_directory = _get_starting_directory(sys.argv)
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
IGNORED_FILES = ('import_path.py', 'indentation.py')
CHECKERS = [Pep8Checker()]


def _should_check(module):
    module_name = os.path.basename(module)
    return module.endswith('.py') and module_name not in IGNORED_FILES


def _run_checker(base_directory, checker):
    LOGGER.info('============Running %s============', checker.checker_name)
    # (top, topdown=True, oneerror=None, followlinks=False)
    # return a 3-tuple (dirpath, dirnames, filenames)
    # can modify dirnames when topdown is True
    for root, _, files in os.walk(base_directory):
        for name in files:
            file_path = os.path.join(root, name)
            if _should_check(file_path):
                LOGGER.info('==checking %s==', file_path)
                checker.check_style(file_path)
            else:
                LOGGER.debug('Ignore %s', file_path)
    LOGGER.info('%s:\n\tPassed: %d; \n\tFailed: %d', checker.checker_name,
                checker.passed, checker.failed)


def main():
    LOGGER.debug('Inspecting in directory %s...', base_directory)
    for checker in CHECKERS:
        _run_checker(base_directory, checker)
    # if any(checker.failed > 0 for checker in CHECKERS):
    #     sys.exit()


if __name__ == '__main__':
    main()
