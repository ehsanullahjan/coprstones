# coprstones

A well-maintained collection of build specs for projects that don't provide official [RPM](https://rpm.org/)s. The repository maintains specs for building native RPM packages via [Fedora COPR](https://copr.fedorainfracloud.org/).

## Available Packages

| Package                      | Description                                                    | Version |
| ---------------------------- | -------------------------------------------------------------- | ------- |
| **[`swayrot8`](./swayrot8)** | Tablet and 2-in-1 laptop auto-rotation daemon for SwayWM       | `1.0.0` |
| **[`wvkbd`](./wvkbd)**       | On-screen keyboard tailored for wlroots compositors (Wayland). | `0.21`  |

## Usage

On Fedora-based systems:

```bash
# Enable the repository
sudo dnf copr enable -y ehsanj/coprstones

# Install one or more of the available packages
sudo dnf install -y wvkbd
```
