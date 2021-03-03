# Python Binary Tree Algorithms
These are some BST algorithms designed to review BSTs.

# Generating a BST for Test Cases
```py
# --------------------------------------------------
# 1. To generate a random BST
python
import binarytree
# binarytree.bst(height=3, is_perfect=False)
bst = binarytree.bst()
bst.values
# 2. To generate a printout for reference
bst.pprint(bst)
# Copy the output value ex. [14, 13, None, 4, None, None, None, 2, 12]
# In test case:
import binarytree
root = binarytree.build([14, 13, None, 4, None, None, None, 2, 12])

# For more see https://binarytree.readthedocs.io/en/latest/specs.html#binarytree.bst
```
### Recommended VS Code Extensions
* `./settings.json` will provide recommended setup. Accept any installs requested to re-use.

# Python3 Installation

## WSL with Ubuntu - Install `pyenv` and required items
1. `pyenv` is installed on latest, and with `pip` and `pipenv` modules (different if not Ubuntu):
```sh
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl https://pyenv.run | bash
```
2. Read the output of the `pyenv` install script, it will ask you to add to `~/.bashrc` and/or `~/.zshrc` the following (different if not on Ubuntu):
```
export PATH="/home/quincy/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
2. ~/.profile or ~/.zshrc contains `pipenv` on `PATH` (different if not Ubuntu):
```sh
#Contents of ~/.profile
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```
3. Enter python dir, use `pipenv` with specified versions (say yes to installign python ver), and run tests with `green`
```sh
cd ./python_leetcode
pipenv --rm
pyenv install
pipenv shell
pipenv install
green
```

## Recommended VS Code Extensions
* Python Test Explorer
* Black formatter

## Recommended zsh Extensions
* [zsh-autoswitch-virtualenv](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv)

### `zsh-autoswitch-virtualenv` Required config for WSL2
1. Open wsl.conf within Ubuntu WSL
```sh
sudo vim /etc/wsl.conf
```
2. `i` for insert, then paste:
```conf
[automount]
enabled = true
options = "metadata"
mountFsTab = false
```
3. Restart
4. If prompted, you can now `chmod 600 ./Pipenv`.