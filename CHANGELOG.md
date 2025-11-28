<!-- markdownlint-disable MD013 -->

# Changelog

## [0.95.0](https://github.com/tiborsimko/reana-workflow-engine-yadage/compare/v0.9.5...0.95.0) (2025-11-28)


### ⚠ BREAKING CHANGES

* **python:** drop support for Python 3.6 and 3.7

### Build

* **docker:** install correct extras of reana-commons submodule ([#256](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/256)) ([8b4caf0](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/8b4caf033a765d2db77942a94a58807ac2230ca7))
* **docker:** non-editable submodules in "latest" mode ([#249](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/249)) ([a57716a](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/a57716a5d7ca6c453f3ed6b977226e47139a9ead))
* **docker:** pin setuptools 70 ([#274](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/274)) ([bc505d8](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/bc505d84a4092610e883e766ad08d2efefe8d908))
* **docker:** pin setuptools to v70 ([#272](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/272)) ([2e30b73](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2e30b73c336ae5e998a3868def0f7cde2c19507c))
* **docker:** upgrade to Ubuntu 24.04 and Python 3.12 ([#271](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/271)) ([54383a5](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/54383a5f8e9e2da5f64b0384b690c8d2a5f48e6b))
* **python:** add minimal `pyproject.toml` ([#272](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/272)) ([424a1a3](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/424a1a3fc9bb3ad0d081ff49e6eb813a262fb131))
* **python:** avoid using requirements.in ([#266](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/266)) ([b9deced](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/b9decedb020d906848cfcb0673d6bf20bc9772c7))
* **python:** bump all required packages as of 2024-03-04 ([#261](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/261)) ([2a02e19](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2a02e19bbf1a3c8b29f8185e4946d382aa8f27e5))
* **python:** bump shared REANA packages as of 2024-03-04 ([#261](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/261)) ([493aee1](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/493aee14c1224d5d961c792cc12d21bff314b007))
* **python:** bump shared REANA packages as of 2024-11-28 ([#276](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/276)) ([5911143](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/59111432c2c5a7fea98a71ffb2d78a9e7c1a47af))
* **python:** drop support for Python 3.6 and 3.7 ([#267](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/267)) ([3320982](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/332098278e4b079b9d04df7e2eec39d40ebd1fcc))
* **python:** remove deprecated `pytest-runner` ([#272](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/272)) ([e64a232](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/e64a23224a80b94180a1abd2678e5af2e9e4fe0f))
* **python:** use jq 1.2.2 on aarch64/arm64 ([#282](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/282)) ([6221c47](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/6221c47ca769f186d0e82279f38b3792ba955e2f))
* **python:** use jq 1.2.2 on aarch64/arm64 ([#282](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/282)) ([0f02e74](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/0f02e7442e062215a3b02d6ac6dd41c47435f43a)), closes [#281](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/281)
* **python:** use optional deps instead of `tests_require` ([#272](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/272)) ([7488b65](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/7488b653d94801844e32c2c51cc7b5871b1b054e))


### Features

* **externalbackend:** allow Compute4PUNCH backend options ([#269](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/269)) ([1ce8e6a](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/1ce8e6a41f14996c50c53fcd7e84565626756ace))
* **externalbackend:** pass K8s requests/limits to job controller ([#279](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/279)) ([6221c47](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/6221c47ca769f186d0e82279f38b3792ba955e2f))
* **externalbackend:** pass K8s requests/limits to job controller ([#279](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/279)) ([994ffa6](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/994ffa639c8b5f0dbe603f56cab30ffe863db3a4))


### Bug fixes

* **progress:** correctly handle running and stopped jobs ([#258](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/258)) ([56ef6a4](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/56ef6a4e434d82d8cfb9916bcfa84a0219bc2e03))
* **tracker:** remove invalid `planned` state ([#268](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/268)) ([b6c0503](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/b6c050302131e63bafbdb164db9b01968785a328)), closes [#255](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/255)


### Code refactoring

* **docs:** move from reST to Markdown ([#259](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/259)) ([37f05e6](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/37f05e6f864c33b721f7926f60d6f68f9d2f841a))


### Continuous integration

* **actions:** update GitHub actions due to Node 16 deprecation ([#265](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/265)) ([95341c8](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/95341c89523528c161061def17c6c174e4beaddf))
* add hadolint and flake8 linters ([1854b6f](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/1854b6f3bb9e59ef95f9faa7899f43399da8ed50))
* added github actions workflow ([bdfc807](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/bdfc80715a9bf66ef8ac2f72c0a27362ae858156))
* **commitlint:** addition of commit message linter ([#251](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/251)) ([f180e21](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/f180e211438df74e23b5f538710d08afb92ae6b2))
* **commitlint:** allow release commit style ([#262](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/262)) ([1b8b6b8](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/1b8b6b87782c4ea006d6bd5ca5b3f2e1bb721287))
* **commitlint:** check for the presence of concrete PR number ([#257](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/257)) ([9ddb488](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/9ddb4885fbc008c25394adde08dd94411217f5fe))
* **commitlint:** fix local running of commit linter on macOS ([#286](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/286)) ([4d2fd09](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/4d2fd091f4ffb53d401530eec5a43814e2be413e))
* **commitlint:** improve checking of merge commits ([#273](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/273)) ([45abc2f](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/45abc2f1dc9fdbbbe4b3c9e3b869149614f5a0f7))
* **jsonlint:** add JSON linting ([#288](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/288)) ([e04c7fa](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/e04c7fabcbce987dc10883f92112ad1a7702ec2f))
* **markdownlint:** add Markdown linting ([#288](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/288)) ([2dd9310](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2dd9310028d82d4aae366212f8fa1ab6692a9b17))
* **prettier:** add Prettier code formatting checks ([#288](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/288)) ([49e092d](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/49e092d5cdb9b7a1c5127cd67e8e038dffbbde69))
* publish docker image after new release ([f01a40a](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/f01a40ade0d0717720e31e3ac83120c7a6a2df85))
* **pytest:** invoke `pytest` directly instead of `setup.py test` ([#272](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/272)) ([2a3db34](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2a3db345b0ad8461c4cdf16b01ddc91bf347ef47))
* **release-please:** initial configuration ([#251](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/251)) ([dc4fa7a](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/dc4fa7a741af36b1fc1968eba18a98597ace26c9))
* **release-please:** update version in Dockerfile ([#254](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/254)) ([8f18751](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/8f18751696f0ebbf5c0d08b08d9c3e58ee3e3897))
* remove older versions from python tests ([6ade095](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/6ade0952e03603c961fdd08ec19e2b742e5d25bb))
* **runners:** upgrade CI runners to Ubuntu 22.04 ([#282](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/282)) ([6221c47](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/6221c47ca769f186d0e82279f38b3792ba955e2f))
* **runners:** upgrade CI runners to Ubuntu 22.04 ([#282](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/282)) ([029019e](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/029019e01343ac39bdadf1c6df347dd2199bcfa3))
* **shellcheck:** fix exit code propagation ([#257](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/257)) ([8831d9e](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/8831d9e319545889b6e4ce1a589e140bb2fa2275))
* **shfmt:** add shell script formatting checks ([#288](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/288)) ([93fee91](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/93fee912cdc860c28ff69fe2b46deaef5441791f))
* temporary pin for setuptools ([652e4c9](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/652e4c9e3730949d38bd3ef8a57be6dc85d38f16))
* update all actions ([cdb6ca0](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/cdb6ca0d08405c12b9b22449bf1c1d5fb1739084))
* **yamllint:** add YAML linting ([#288](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/288)) ([c9a5399](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/c9a5399327d6f64aeb27c67efaa42600fa563176))


### Documentation

* add .readthedocs.yaml to migrate to RTD v2 ([41ead44](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/41ead443cbcfc0f9fc92d3b30420239e4f21acc4))
* author ORCID links ([00af163](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/00af163971a472a7f7e92f3a569ed7b58bdd1e20))
* **authors:** complete list of contributors ([#260](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/260)) ([68f97a0](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/68f97a0aff07b16e2707423185925c8d6d22c33b))
* autodoc_mock_imports for jq ([2cc5598](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2cc55986ce15e9d24907af4a0234f8069fe60338)), closes [#163](https://github.com/tiborsimko/reana-workflow-engine-yadage/issues/163)
* better structure ([93b7b9b](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/93b7b9bc79531e80be6b28dbff954bb16d8387f8))
* initial release ([8934720](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/8934720cae8b043471921f1685c93fcbfe802fcf))
* new logo, panel verbiage and links ([6d62abf](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/6d62abfce9b94b58145fd96865746d35b2af22b6))
* readme badge typo ([8cbfd83](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/8cbfd835e57f8320be4deff9941d01a60ba96573))
* set default language to English ([28efeec](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/28efeeccee2683a0592fd3bb7164bda36bd1a6ed))
* single-page RTFD outline ([5cb97e0](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/5cb97e06c5cb87309177a24fb0db2ee754fbf567))
* standardised list itemisation ([ca17d07](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/ca17d079fb6cb649eeb066241a20e4334a74f4bf))
* structure improvements and new chapters ([2c6801e](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/2c6801e9f563590b7aa1c314a45cc370e834d427))
* update changelog ([b054264](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/b054264eccb4b03eebcae9b64ec02b68005ee703))


### Chores

* **master:** release 0.95.0-alpha.1 ([ed93cfa](https://github.com/tiborsimko/reana-workflow-engine-yadage/commit/ed93cfa1f49c1e16a8f8e294740bbf2c1ab22fb0))

## [0.9.5](https://github.com/reanahub/reana-workflow-engine-yadage/compare/0.9.4...0.9.5) (2024-11-29)

### Build

* **docker:** pin setuptools 70 ([#274](https://github.com/reanahub/reana-workflow-engine-yadage/issues/274)) ([bc505d8](https://github.com/reanahub/reana-workflow-engine-yadage/commit/bc505d84a4092610e883e766ad08d2efefe8d908))
* **python:** bump shared REANA packages as of 2024-11-28 ([#276](https://github.com/reanahub/reana-workflow-engine-yadage/issues/276)) ([5911143](https://github.com/reanahub/reana-workflow-engine-yadage/commit/59111432c2c5a7fea98a71ffb2d78a9e7c1a47af))

### Features

* **externalbackend:** allow Compute4PUNCH backend options ([#269](https://github.com/reanahub/reana-workflow-engine-yadage/issues/269)) ([1ce8e6a](https://github.com/reanahub/reana-workflow-engine-yadage/commit/1ce8e6a41f14996c50c53fcd7e84565626756ace))

## [0.9.4](https://github.com/reanahub/reana-workflow-engine-yadage/compare/0.9.3...0.9.4) (2024-03-04)

### Build

* **docker:** install correct extras of reana-commons submodule ([#256](https://github.com/reanahub/reana-workflow-engine-yadage/issues/256)) ([8b4caf0](https://github.com/reanahub/reana-workflow-engine-yadage/commit/8b4caf033a765d2db77942a94a58807ac2230ca7))
* **docker:** non-editable submodules in "latest" mode ([#249](https://github.com/reanahub/reana-workflow-engine-yadage/issues/249)) ([a57716a](https://github.com/reanahub/reana-workflow-engine-yadage/commit/a57716a5d7ca6c453f3ed6b977226e47139a9ead))
* **python:** bump all required packages as of 2024-03-04 ([#261](https://github.com/reanahub/reana-workflow-engine-yadage/issues/261)) ([2a02e19](https://github.com/reanahub/reana-workflow-engine-yadage/commit/2a02e19bbf1a3c8b29f8185e4946d382aa8f27e5))
* **python:** bump shared REANA packages as of 2024-03-04 ([#261](https://github.com/reanahub/reana-workflow-engine-yadage/issues/261)) ([493aee1](https://github.com/reanahub/reana-workflow-engine-yadage/commit/493aee14c1224d5d961c792cc12d21bff314b007))

### Bug fixes

* **progress:** correctly handle running and stopped jobs ([#258](https://github.com/reanahub/reana-workflow-engine-yadage/issues/258)) ([56ef6a4](https://github.com/reanahub/reana-workflow-engine-yadage/commit/56ef6a4e434d82d8cfb9916bcfa84a0219bc2e03))

### Code refactoring

* **docs:** move from reST to Markdown ([#259](https://github.com/reanahub/reana-workflow-engine-yadage/issues/259)) ([37f05e6](https://github.com/reanahub/reana-workflow-engine-yadage/commit/37f05e6f864c33b721f7926f60d6f68f9d2f841a))

### Continuous integration

* **commitlint:** addition of commit message linter ([#251](https://github.com/reanahub/reana-workflow-engine-yadage/issues/251)) ([f180e21](https://github.com/reanahub/reana-workflow-engine-yadage/commit/f180e211438df74e23b5f538710d08afb92ae6b2))
* **commitlint:** allow release commit style ([#262](https://github.com/reanahub/reana-workflow-engine-yadage/issues/262)) ([1b8b6b8](https://github.com/reanahub/reana-workflow-engine-yadage/commit/1b8b6b87782c4ea006d6bd5ca5b3f2e1bb721287))
* **commitlint:** check for the presence of concrete PR number ([#257](https://github.com/reanahub/reana-workflow-engine-yadage/issues/257)) ([9ddb488](https://github.com/reanahub/reana-workflow-engine-yadage/commit/9ddb4885fbc008c25394adde08dd94411217f5fe))
* **release-please:** initial configuration ([#251](https://github.com/reanahub/reana-workflow-engine-yadage/issues/251)) ([dc4fa7a](https://github.com/reanahub/reana-workflow-engine-yadage/commit/dc4fa7a741af36b1fc1968eba18a98597ace26c9))
* **release-please:** update version in Dockerfile ([#254](https://github.com/reanahub/reana-workflow-engine-yadage/issues/254)) ([8f18751](https://github.com/reanahub/reana-workflow-engine-yadage/commit/8f18751696f0ebbf5c0d08b08d9c3e58ee3e3897))
* **shellcheck:** fix exit code propagation ([#257](https://github.com/reanahub/reana-workflow-engine-yadage/issues/257)) ([8831d9e](https://github.com/reanahub/reana-workflow-engine-yadage/commit/8831d9e319545889b6e4ce1a589e140bb2fa2275))

### Documentation

* **authors:** complete list of contributors ([#260](https://github.com/reanahub/reana-workflow-engine-yadage/issues/260)) ([68f97a0](https://github.com/reanahub/reana-workflow-engine-yadage/commit/68f97a0aff07b16e2707423185925c8d6d22c33b))

## 0.9.3 (2023-12-14)

* Changes `jq` dependency version on amd64 architecture to older version, making certain Yadage workflows much faster.

## 0.9.2 (2023-12-12)

* Adds automated multi-platform container image building for amd64 and arm64 architectures.
* Adds metadata labels to Dockerfile.
* Fixes container image building on the arm64 architecture.

## 0.9.1 (2023-09-27)

* Fixes container image names to be Podman-compatible.

## 0.9.0 (2023-01-19)

* Adds support for specifying `slurm_partition` and `slurm_time` for Slurm compute backend jobs.
* Adds support for Kerberos authentication for workflow orchestration.
* Adds support for Rucio authentication for workflow jobs.
* Changes the base image of the component to Ubuntu 20.04 LTS and reduces final Docker image size by removing build-time dependencies.

## 0.8.2 (2022-02-08)

* Changes dependencies to solve compatibility issues with `Yadage 0.20.2` version.

## 0.8.1 (2022-02-07)

* Adds support for specifying `kubernetes_job_timeout` for Kubernetes compute backend jobs.
* Fixes workflow stuck in pending status due to early Yadage fail.

## 0.8.0 (2021-11-22)

* Adds users quota accounting.
* Changes workflow specification loading to be done in `reana-commons`.
* Changes workflow engine to reduce the number of API calls to REANA-Job-Controller.
* Changes workflow engine to remove duplicated messages to the job status message queue.

## 0.7.5 (2021-07-05)

* Changes internal dependencies to remove click.

## 0.7.4 (2021-04-28)

* Adds support for specifying `kubernetes_memory_limit` for Kubernetes compute backend jobs.

## 0.7.3 (2021-03-17)

* Changes workflow engine instantiation to use central REANA-Commons factory.
* Changes job command strings by removing interpreter when possible and using central REANA-Commons job command serialisation.

## 0.7.2 (2021-02-03)

* Fixes minor code warnings.
* Changes CI system to include Python flake8 and Dockerfile hadolint checkers.

## 0.7.1 (2020-11-10)

* Adds support for specifying `htcondor_max_runtime` and `htcondor_accounting_group` for HTCondor compute backend jobs.
* Fixes restarting of Yadage workflows.

## 0.7.0 (2020-10-20)

* Adds creation of workflow visualisation graph by default when a workflow runs.
* Adds option to specify unpacked Docker images as workflow step requirement.
* Adds handling of workflow specification load logic that was done before in `reana-client`.
* Adds support for VOMS proxy as a new authentication method.
* Adds support for `initfiles` operational option.
* Adds pinning of all Python dependencies allowing to easily rebuild component images at later times.
* Changes Yadage workflow engine to version 0.20.1.
* Changes base image to use Python 3.8.
* Changes code formatting to respect `black` coding style.
* Changes documentation to single-page layout.

## 0.6.1 (2020-05-25)

* Upgrades REANA-Commons package using latest Kubernetes Python client version.

## 0.6.0 (2019-12-20)

* Allows to specify compute backend (HTCondor, Kubernetes or Slurm) and
  Kerberos authentication requirement for Yadage workflow jobs.
* Upgrades Python to 3.6.
* Upgrades Yadage to 0.20.0.
* Upgrades Packtivity to 0.14.21.
* Sets default umask 002 for jobs writing to the workflow workspace.
* Allows setting UID for the job container runtime user.
* Moves workflow engine to the same Kubernetes pod with the REANA-Job-Controller
  (sidecar pattern).

## 0.5.0 (2019-04-23)

* Makes workflow engine independent of Celery so that independent workflow
  instances are created on demand for each user.
* Centralises the initialisation of `WorkflowStatusPublisher`.
* Introduces CVMFS mounts in job specifications.
* Makes docker image slimmer by using `python:2.7-slim`.
* Centralises log level and log format configuration.

## 0.4.0 (2018-11-06)

* Improves AMQP re-connection handling. Switches from `pika` to `kombu`.
* Utilises common openapi client for communication with REANA-Job-Controller.
* Changes license to MIT.

## 0.3.1 (2018-09-07)

* Pins REANA-Commons and Celery dependencies.

## 0.3.0 (2018-08-10)

* Tracks workflow progress.

## 0.2.0 (2018-04-19)

* Upgrades Yadage workflow ecosystem versions (Yadage 0.13, Packtivity 0.10).
* Adds logs to the workflow models in the database.

## 0.1.0 (2018-01-30)

* Initial public release.
