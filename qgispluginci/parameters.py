#!/usr/bin/python3

import os
from slugify import slugify


class Parameters:
    """
    Attributes
    ----------
    plugin_name: str
        The human readable plugin name
        e.g. 'My Super Plugin'

    src_dir: str
        The directory of the source code in the repository.
        Defaults to: `slugify(plugin_name, separator='_')`

    plugin_main_file: str
        The name of the plugin main Python file.
        Defaults to: `'{}_plugin.py'.format(slugify(self.plugin_name, separator='_'))`

    release_version: str
        The release version.
        e.g. 1.2.3
        This will be used as plugin version when packaging the plugin and in SCM host (Github only for now)

    organization_slug: str
        The organization slug on SCM host (e.g. Github) and translation platform (e.g. Transifex).
        Not required when running on Travis since deduced from `$TRAVIS_REPO_SLUG`environment variable.
        
    project_slug: str
        The project slug on SCM host (e.g. Github) and translation platform (e.g. Transifex).
        Not required when running on Travis since deduced from `$TRAVIS_REPO_SLUG`environment variable.
        Otherwise, defaults to
        
    transifex_token: str
        The API token required for translations.

    transifex_coordinator: str
        The username of the coordinator in Transifex.
        Required to create new languages.

    transifex_organization: str
        The organization name in Transifex
        Defaults to: `organization`

    translation_source_language:
        The source language for translations.
        Defaults to: 'en'

    repository_url: str
        The repository URL. Will be deduced if run on Travis.
        Required to create new resources on Transifex.

    lrelease_path: str
        The path of lrelease executable

    pylupdate5_path: str
        The path of pylupdate executable


    """
    def __init__(self, definition: dict):
        self.plugin_name = definition['plugin_name']
        self.release_version = definition.get('release_version')
        self.src_dir = definition.get('src_dir', slugify(self.plugin_name, separator='_'))
        self.plugin_main_file = definition.get('plugin_main_file', '{}_plugin.py'.format(slugify(self.plugin_name, separator='_')))
        self.organization_slug = definition.get('organization_slug', os.environ.get('TRAVIS_REPO_SLUG', '').split('/')[0])
        self.project_slug = definition.get('project_slug', os.environ.get('TRAVIS_REPO_SLUG', '.../{}'.format(slugify(self.plugin_name))).split('/')[1])
        self.transifex_token = definition.get('transifex_token', '')
        self.transifex_coordinator = definition.get('transifex_coordinator', '')
        self.transifex_organization = definition.get('transifex_organization', self.organization_slug)
        self.translation_source_language = definition.get('translation_source_language', 'en')
        self.translation_languages = definition.get('translation_languages', {})
        self.repository_url = definition.get('repository_url', 'https://www.github.com/{s}'.format(s=os.environ.get('TRAVIS_REPO_SLUG')))
        self.lrelease_path = definition.get('lrelease_path', 'lrelease')
        self.pylupdate5_path = definition.get('pylupdate5_path', 'pylupdate5')