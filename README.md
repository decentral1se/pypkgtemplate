# pypkgtemplate

> A Python package cookiecutter with modern tooling

## Why another template?

A lot of cookiecutter template designers try to include **all** the things from
the start and then due to maintenance burdens, the package template fall behind
with the moving ecosystem. For example, one of the most commonly used packages,
`cookiecutter-pypackage` has, at present moment, not been updated for a year
and has 23 open change requests.

This template is about moving with the ecosystem to provide a modern and
up-to-date cookiecutter template for creating Python packages. In order to keep
up to speed, I focus on tooling configuration rather than code customisation.
Your Python package code can be different each time but the tools should be
standardised and reliable.

## Usage

```sh
$ python -m pip install --user pipx
$ pipx install cookiecutter
$ cookiecutter https://git.autonomic.zone/decentral1se/pypkgtemplate.git
```

## Variables

```json
{
  "package": "",
  "package_description": "",
  "author": "",
  "author_email": "",
  "git_hosting_url": ""
}
```

- **package**: The package name.
- **package_description**: The package short description.
- **author**: The package creator.
- **author_email**: The package creator's email.
- **git_hosting_url**: The git hosting URL of the package.
