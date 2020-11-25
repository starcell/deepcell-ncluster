#
# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest


validator_json = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Jupyter Notebook v4.2 JSON schema.",
    "type": "object",
    "additionalProperties": "false",
    "required": ["metadata", "nbformat_minor", "nbformat", "cells"],
    "properties": {
        "metadata": {
            "description": "Notebook root-level metadata.",
            "type": "object",
            "additionalProperties": "true",
            "properties": {
                "kernelspec": {
                    "description": "Kernel information.",
                    "type": "object",
                    "required": ["name", "display_name"],
                    "properties": {
                        "name": {
                            "description": "Name of the kernel specification.",
                            "type": "string"
                        },
                        "display_name": {
                            "description": "Name to display in UI.",
                            "type": "string"
                        }
                    }
                },
                "language_info": {
                  "description": "Kernel information.",
                  "type": "object",
                  "required": ["name"],
                  "properties": {
                    "name": {
                        "description": "The programming language which this kernel runs.",
                        "type": "string"
                    },
                    "codemirror_mode": {
                        "description": "The codemirror mode to use for code in this language.",
                        "oneOf": [
                          {"type": "string"},
                          {"type": "object"}
                        ]
                    },
                    "file_extension": {
                        "description": "The file extension for files in this language.",
                        "type": "string"
                    },
                    "mimetype": {
                        "description": "The mimetype corresponding to files in this language.",
                        "type": "string"
                    },
                    "pygments_lexer": {
                        "description": "The pygments lexer to use for code in this language.",
                        "type": "string"
                    }
                  }
                },
                "orig_nbformat": {
                    "description": "Original notebook format (major number) before converting the notebook "
                                   "between versions. This should never be written to a file.",
                    "type": "integer",
                    "minimum": 1
                },
                "title": {
                    "description": "The title of the notebook document",
                    "type": "string"
                },
                "authors": {
                    "description": "The author(s) of the notebook document",
                    "type": "array",
                    "item": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": "true"
                    }
                }
            }
        },
        "nbformat_minor": {
            "description": "Notebook format (minor number). Incremented for backward compatible changes "
                           "to the notebook format.",
            "type": "integer",
            "minimum": 0
        },
        "nbformat": {
            "description": "Notebook format (major number). Incremented between backwards incompatible "
                           "changes to the notebook format.",
            "type": "integer",
            "minimum": 4,
            "maximum": 4
        },
        "cells": {
            "description": "Array of cells of the current notebook.",
            "type": "array",
            "items": {"$ref": "#/definitions/cell"}
        }
    },

    "definitions": {
        "cell": {
            "type": "object",
            "oneOf": [
                {"$ref": "#/definitions/raw_cell"},
                {"$ref": "#/definitions/markdown_cell"},
                {"$ref": "#/definitions/code_cell"}
            ]
        },

        "raw_cell": {
            "description": "Notebook raw nbconvert cell.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["cell_type", "metadata", "source"],
            "properties": {
                "cell_type": {
                    "description": "String identifying the type of cell.",
                    "enum": ["raw"]
                },
                "metadata": {
                    "description": "Cell-level metadata.",
                    "type": "object",
                    "additionalProperties": "true",
                    "properties": {
                        "format": {
                            "description": "Raw cell metadata format for nbconvert.",
                            "type": "string"
                        },
                        "jupyter": {
                          "description": "Official Jupyter Metadata for Raw Cells",
                          "type": "object",
                          "additionalProperties": "true",
                          "source_hidden": {
                                "description": "Whether the source is hidden.",
                                "type": "boolean"
                          }
                        },
                        "name": {"$ref": "#/definitions/misc/metadata_name"},
                        "tags": {"$ref": "#/definitions/misc/metadata_tags"}
                    }
                },
                "attachments": {"$ref": "#/definitions/misc/attachments"},
                "source": {"$ref": "#/definitions/misc/source"}
            }
        },

        "markdown_cell": {
            "description": "Notebook markdown cell.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["cell_type", "metadata", "source"],
            "properties": {
                "cell_type": {
                    "description": "String identifying the type of cell.",
                    "enum": ["markdown"]
                },
                "metadata": {
                    "description": "Cell-level metadata.",
                    "type": "object",
                    "properties": {
                        "name": {"$ref": "#/definitions/misc/metadata_name"},
                        "tags": {"$ref": "#/definitions/misc/metadata_tags"},
                        "jupyter": {
                          "description": "Official Jupyter Metadata for Markdown Cells",
                          "type": "object",
                          "additionalProperties": "true",
                            "source_hidden": {
                                "description": "Whether the source is hidden.",
                                "type": "boolean"
                            }
                        }
                    },
                    "additionalProperties": "true"
                },
                "attachments": {"$ref": "#/definitions/misc/attachments"},
                "source": {"$ref": "#/definitions/misc/source"}
            }
        },

        "code_cell": {
            "description": "Notebook code cell.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["cell_type", "metadata", "source", "outputs", "execution_count"],
            "properties": {
                "cell_type": {
                    "description": "String identifying the type of cell.",
                    "enum": ["code"]
                },
                "metadata": {
                    "description": "Cell-level metadata.",
                    "type": "object",
                    "additionalProperties": "true",
                    "properties": {
                        "jupyter": {
                          "description": "Official Jupyter Metadata for Code Cells",
                          "type": "object",
                          "additionalProperties": "true",
                          "source_hidden": {
                                "description": "Whether the source is hidden.",
                                "type": "boolean"
                           },
                          "outputs_hidden": {
                                "description": "Whether the outputs are hidden.",
                                "type": "boolean"
                           }
                        },
                        "collapsed": {
                            "description": "Whether the cell is collapsed/expanded.",
                            "type": "boolean"
                        },
                        "scrolled": {
                            "description": "Whether the cell's output is scrolled, unscrolled, or autoscrolled.",
                            "enum": ["true", "false", "auto"]
                        },
                        "name": {"$ref": "#/definitions/misc/metadata_name"},
                        "tags": {"$ref": "#/definitions/misc/metadata_tags"}
                    }
                },
                "source": {"$ref": "#/definitions/misc/source"},
                "outputs": {
                    "description": "Execution, display, or stream outputs.",
                    "type": "array",
                    "items": {"$ref": "#/definitions/output"}
                },
                "execution_count": {
                    "description": "The code cell's prompt number. Will be null if the cell has not been run.",
                    "type": ["integer", "null"],
                    "minimum": 0
                }
            }
        },

        "unrecognized_cell": {
            "description": "Unrecognized cell from a future minor-revision to the notebook format.",
            "type": "object",
            "additionalProperties": "true",
            "required": ["cell_type", "metadata"],
            "properties": {
                "cell_type": {
                    "description": "String identifying the type of cell.",
                    "not": {
                      "enum": ["markdown", "code", "raw"]
                    }
                },
                "metadata": {
                    "description": "Cell-level metadata.",
                    "type": "object",
                    "properties": {
                        "name": {"$ref": "#/definitions/misc/metadata_name"},
                        "tags": {"$ref": "#/definitions/misc/metadata_tags"}
                    },
                    "additionalProperties": "true"
                }
            }
        },

        "output": {
            "type": "object",
            "oneOf": [
                {"$ref": "#/definitions/execute_result"},
                {"$ref": "#/definitions/display_data"},
                {"$ref": "#/definitions/stream"},
                {"$ref": "#/definitions/error"}
            ]
        },

        "execute_result": {
            "description": "Result of executing a code cell.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["output_type", "data", "metadata", "execution_count"],
            "properties": {
                "output_type": {
                    "description": "Type of cell output.",
                    "enum": ["execute_result"]
                },
                "execution_count": {
                    "description": "A result's prompt number.",
                    "type": ["integer", "null"],
                    "minimum": 0
                },
                "data": {"$ref": "#/definitions/misc/mimebundle"},
                "metadata": {"$ref": "#/definitions/misc/output_metadata"}
            }
        },

        "display_data": {
            "description": "Data displayed as a result of code cell execution.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["output_type", "data", "metadata"],
            "properties": {
                "output_type": {
                    "description": "Type of cell output.",
                    "enum": ["display_data"]
                },
                "data": {"$ref": "#/definitions/misc/mimebundle"},
                "metadata": {"$ref": "#/definitions/misc/output_metadata"}
            }
        },

        "stream": {
            "description": "Stream output from a code cell.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["output_type", "name", "text"],
            "properties": {
                "output_type": {
                    "description": "Type of cell output.",
                    "enum": ["stream"]
                },
                "name": {
                    "description": "The name of the stream (stdout, stderr).",
                    "type": "string"
                },
                "text": {
                    "description": "The stream's text output, represented as an array of strings.",
                    "$ref": "#/definitions/misc/multiline_string"
                }
            }
        },

        "error": {
            "description": "Output of an error that occurred during code cell execution.",
            "type": "object",
            "additionalProperties": "false",
            "required": ["output_type", "ename", "evalue", "traceback"],
            "properties": {
                "output_type": {
                    "description": "Type of cell output.",
                    "enum": ["error"]
                },
                "ename": {
                    "description": "The name of the error.",
                    "type": "string"
                },
                "evalue": {
                    "description": "The value, or message, of the error.",
                    "type": "string"
                },
                "traceback": {
                    "description": "The error's traceback, represented as an array of strings.",
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },

        "unrecognized_output": {
            "description": "Unrecognized output from a future minor-revision to the notebook format.",
            "type": "object",
            "additionalProperties": "true",
            "required": ["output_type"],
            "properties": {
                "output_type": {
                    "description": "Type of cell output.",
                    "not": {
                        "enum": ["execute_result", "display_data", "stream", "error"]
                    }
                }
            }
        },

        "misc": {
            "metadata_name": {
                "description": "The cell's name. If present, must be a non-empty string. Cell names are "
                               "expected to be unique across all the cells in a given notebook. This criterion cannot "
                               "be checked by the json schema and must be established by an additional check.",
                "type": "string",
                "pattern": "^.+$"
            },
            "metadata_tags": {
                "description": "The cell's tags. Tags must be unique, and must not contain commas.",
                "type": "array",
                "uniqueItems": "true",
                "items": {
                    "type": "string",
                    "pattern": "^[^,]+$"
                }
            },
            "attachments": {
                "description": "Media attachments (e.g. inline images), stored as mimebundle keyed by filename.",
                "type": "object",
                "patternProperties": {
                    ".*": {
                        "description": "The attachment's data stored as a mimebundle.",
                        "$ref": "#/definitions/misc/mimebundle"
                    }
                }
            },
            "source": {
                "description": "Contents of the cell, represented as an array of lines.",
                "$ref": "#/definitions/misc/multiline_string"
            },
            "execution_count": {
                "description": "The code cell's prompt number. Will be null if the cell has not been run.",
                "type": ["integer", "null"],
                "minimum": 0
            },
            "mimebundle": {
                "description": "A mime-type keyed dictionary of data",
                "type": "object",
                "additionalProperties": {
                  "description": "mimetype output (e.g. text/plain), represented as either an array "
                                 "of strings or a string.",
                  "$ref": "#/definitions/misc/multiline_string"
                },
                "patternProperties": {
                    "^application/(.*\\+)?json$": {
                        "description": "Mimetypes with JSON output, can be any type"
                    }
                }
            },
            "output_metadata": {
                "description": "Cell output metadata.",
                "type": "object",
                "additionalProperties": "true"
            },
            "multiline_string": {
                "oneOf": [
                    {"type": "string"},
                    {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                ]
            }
        }
    }
}


@pytest.fixture
def create_nb_format_mocks(mocker):
    mocker.patch("nbformat.validator._get_schema_json", return_value=validator_json)
    mock_write = mocker.patch("nbformat.write")

    return mock_write
