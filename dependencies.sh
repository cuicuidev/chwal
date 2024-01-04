if python --version 2>&1 | grep -q 'Python 3'; then
	echo "Python 3 is already installed"
else
	echo "A Python 3 installation is required"
	exit 1
fi

if pip --version 2>&1 | grep -q 'python 3'; then
	echo "Pip 3 is already installed"
else
	echo "A Pip 3 installation is required"
	exit 1
fi

if pip3 freeze | grep -q 'pywal'; then
	echo "Pywal is already installed"
else
	echo "A Pywal installation is required"
	exit 1
fi
