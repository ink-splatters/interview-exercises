# Building the project

## Natively on Host

### Prerequsites / Caveats

- **c++17 toolchain is installed**
- make sure you have _Python 3.8+_ installed (lower versions may work but haven't been checked)
- **Windows is not supported, especially natively**


### Setting up `Poetry`

`Poetry` used as package manager as it was planned to use Conan API directly
an there is a nice CLI util in progrss for it (TODO)

#### Using `pipx` [recommended]
```bash
pip install -U wheel setuptools pipx
pipx install poetry
```

#### Using `venv`
```bash
mkdir -p ~/.venvs/greeter
python3 -m venvs ~/.venvs/greeter

source ~/.venvs/greeter/activate.sh
# or source ~/.venvs/greeter/activate.fish if you have fish shell

pip install poetry
# next it's assumed this venv is being used
```

### Preparing the environment
```bash
cd interview-exercises
poetry shell
poetry install

# it's assumed after this point poetry shell is still active when you proceed further
```

### Building *greeting* conan package

## for testing purposes

```bash
cd interview-excersies/libgreeting
./packer.sh dev
```

## exporting the package

```bash
cd interview-excersies/libgreeting
./packer.sh
```

package should be exported as `greeting/0.1.0@ink-splatters/testing

**WARNING: this does not work for now ()**

I'm debugging the next issue:

```
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /Users/inksplatters/dev/interview-exercises/libgreeting/build/package/lib/libgreeting.a
conanfile.py (greeting/0.1.0) package(): Packaged 1 '.a' file: libgreeting.a
conanfile.py (greeting/0.1.0): Package 'package' created
conanfile.py (greeting/0.1.0): Created package revision 42ab58ddeeb8cf8ee9a23e2f6f2893d8
ERROR: package folder definition incompatible with build and source folders
```

### in development mode


## In Docker

### Prerequsites / Caveats
- **IN PROGRESS, being finished ASAP, DOES NOT WORK YET**
- `Docker for Mac` or alternative installation for your system **supporting buildkit** (recent)


### Building 

```bash
cd interview-excersies/libgreeting
docker build -t libgreeting -v$(pwd):/code
# TODO: entrypoint mode
docker run -it 
```

TODO