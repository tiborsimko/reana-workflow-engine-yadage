# This file is part of REANA.
# Copyright (C) 2021, 2025 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Workflow-Engine-Yadage ExternalBackend tests."""

from typing import List, Dict, Any, Union

import pytest


class TestExternalBackend:
    @pytest.mark.parametrize(
        "input_parameters,final_parameters",
        [
            (
                [
                    {"compute_backend": "kubernetes"},
                    {"not_exists": "value"},
                    {"kubernetes_job_timeout": 20},
                    {"kubernetes_cpu_request": None},
                    {"kubernetes_cpu_limit": None},
                    {"kubernetes_memory_request": None},
                    {"kubernetes_memory_limit": None},
                ],
                {
                    "compute_backend": "kubernetes",
                    "kubernetes_job_timeout": 20,
                    "kerberos": False,
                },
            ),
            (
                [{"kubernetes_job_timeout": 10}, {"kubernetes_job_timeout": 30}],
                {"kubernetes_job_timeout": 30, "kerberos": False},
            ),
            (
                [{"kerberos": True}],
                {"kerberos": True},
            ),
        ],
    )
    def test_get_resources(
        self, input_parameters: List[Union[Dict, Any]], final_parameters: Dict[str, Any]
    ):
        from reana_workflow_engine_yadage.externalbackend import ExternalBackend

        assert ExternalBackend._get_resources(input_parameters) == final_parameters
