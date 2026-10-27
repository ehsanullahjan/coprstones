# coprstones

A well-maintained collection of build specs for projects that don't provide official [RPM](https://rpm.org/)s. The repository maintains specs for building native RPM packages via [Fedora COPR](https://copr.fedorainfracloud.org/).

## Available Packages

| Package                | Description                                                    | Version |
| ---------------------- | -------------------------------------------------------------- | ------- |
| **[`wvkbd`](./wvkbd)** | On-screen keyboard tailored for wlroots compositors (Wayland). | `0.21`  |

## Usage

To use these packages on a Fedora-based system:

```bash
# Enable the repository
sudo dnf copr enable -y ehsanj/coprstones

# Install packages
sudo dnf install -y wvkbd
```
