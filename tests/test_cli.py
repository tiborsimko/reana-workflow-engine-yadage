# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Workflow-Engine-Yadage CLI tests."""

from pathlib import Path

import pytest
from yadage.steering_api import steering_ctx


class _Stop(Exception):
    """Stop after the steering context is created."""


def test_steering_ctx_accepts_bare_workspace_path(tmp_path):
    """Test that Yadage accepts the bare workspace path passed by the engine."""
    workspace = str(tmp_path)
    # Raising inside the context skips the workflow run, so that only the
    # creation of the steering object from the bare workspace path is tested.
    with pytest.raises(_Stop):
        with steering_ctx(
            dataarg=workspace,
            dataopts={"initdir": workspace},
            workflow_json={"stages": []},
            visualize=False,
        ) as ys:
            assert Path(ys.metadir) == tmp_path / "_yadage"
            raise _Stop()
