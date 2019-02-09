#
# This file is part of rasa-pipelined.
#
# rasa-pipelined is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasa-pipelined is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasa-pipelined.  If not, see <http://www.gnu.org/licenses/>.

"""Validation schema used by opsd to verify observation schedule blocks"""

# pylint: disable=invalid-name

def configure_flats_validation_schema():
    """Path and Prefix are the only valid user-configurable properties when taking flats"""
    return {
        'type': 'object',
        'additionalProperties': False,
        'properties': {
            'path': {
                'type': 'string',
            },
            'prefix': {
                'type': 'string'
            },
        }
    }

def configure_standard_validation_schema():
    """Standard observations support all properties"""
    return {
        'type': 'object',
        'additionalProperties': False,
        'required': ['type'],
        'properties': {
            'path': {
                'type': 'string',
            },
            'prefix': {
                'type': 'string'
            },
            'type': {
                'type': 'string',
                'enum': ['BIAS', 'DARK', 'FLAT', 'SCIENCE', 'JUNK']
            },
            'object': {
                'type': 'string'
            },
            'archive': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'RASA': {'type': 'boolean'}
                },
            },
            'wcs': {
                'type': 'boolean'
            },
            'intstats': {
                'type': 'boolean'
            },
            'hfd': {
                'type': 'boolean'
            },
            'compression': {
                'type': 'boolean'
            }
        },
        'allOf': [
            {
                'anyOf': [
                    {
                        'not': {
                            'properties': {
                                'type': { 'enum': ['SCIENCE'] }
                            },
                        }
                    },
                    {
                        'required': ['object']
                    },
                ]
            },
            {
                'anyOf': [
                    {
                        'properties': {
                            'archive': {
                                'properties': {
                                    'RASA': {'enum': [False]}
                                }
                            }
                        }
                    },
                    {
                        'required': ['prefix']
                    }
                ]
            }
        ]
    }
