from __future__ import annotations

import os
import sys

import django
from django.test.runner import DiscoverRunner


def func_main(django_settings_module: str, *project_tests: str):
    """Directly set DJANGO_SETTINGS_MODULE instead of
    using settings.configure.

    Test labels given on the command line override `project_tests`, so
    a single module, class or test can be run without editing
    `runtests.py`. With none given, `project_tests` runs as before.
    """
    os.environ["DJANGO_SETTINGS_MODULE"] = django_settings_module
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = any([True for t in sys.argv if t.startswith("--failfast")])
    keepdb = any([True for t in sys.argv if t.startswith("--keepdb")])
    opts = dict(failfast=failfast, tags=tags, keepdb=keepdb)
    # argv[0] is the script itself, and options are handled above
    test_labels = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    failures = DiscoverRunner(**opts).run_tests(test_labels or list(project_tests))
    sys.exit(failures)
