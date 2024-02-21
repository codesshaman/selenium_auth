name = Selenium
APPNAME:=$(word 2, $(MAKECMDGOALS))
DIR := $(abspath $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
VENV_DIR=.venv
VENV=$(DIR)/$(VENV_DIR)
VENV_BIN=$(VENV)/bin
PYTHON=$(VENV_BIN)/python3
PIP=$(VENV_BIN)/pip3

NO_COLOR=\033[0m	    # Color Reset
COLOR_OFF='\e[0m'       # Color Off
OK_COLOR=\033[32;01m	# Green Ok
ERROR_COLOR=\033[31;01m	# Error red
WARN_COLOR=\033[33;01m	# Warning yellow
RED='\e[1;31m'          # Red
GREEN='\e[1;32m'        # Green
YELLOW='\e[1;33m'       # Yellow
BLUE='\e[1;34m'         # Blue
PURPLE='\e[1;35m'       # Purple
CYAN='\e[1;36m'         # Cyan
WHITE='\e[1;37m'        # White
UCYAN='\e[4;36m'        # Cyan

all:
	@printf "$(OK_COLOR)==== Launch main application ====$(NO_COLOR)\n"
	$(PYTHON) main.py;

freeze:
	@$(PIP) freeze

help:
	@echo -e "$(OK_COLOR)==== All commands of ${name} configuration ====$(NO_COLOR)"
	@echo -e "$(WARN_COLOR)- make freeze		        	: Pip freeze command"
	@echo -e "$(WARN_COLOR)- make				        : Launch main script"
	@echo -e "$(WARN_COLOR)- make help				: Makefile commands reference"
	@echo -e "$(WARN_COLOR)- make install <libname>		: Launch pip install"
	@echo -e "$(WARN_COLOR)- make generate				: Generate new gRPC with proto"
	@echo -e "$(WARN_COLOR)- make push				: Push code to repository"
	@echo -e "$(WARN_COLOR)- make req				: Install pip requirements"
	@echo -e "$(WARN_COLOR)- make run <script>			: Launch python script"
	@echo -e "$(WARN_COLOR)- make venv				: Create virtual environment"
	@echo -e "$(WARN_COLOR)- make clean				: Remove python cache"
	@echo -e "$(WARN_COLOR)- make fclean				: Remove venv configuration$(NO_COLOR)"

install:
	@printf "$(OK_COLOR)==== Launch pip install ====$(NO_COLOR)\n"
	@printf "$(OK_COLOR)==== Downloading a new library ====$(NO_COLOR)\n"
	@$(eval args := $(words $(filter-out --,$(MAKECMDGOALS))))
	@if [ "${args}" -eq 2 ]; then \
		echo "$(OK_COLOR) Downloading the library ${APPNAME}$(NO_COLOR)\n"; \
		$(PIP) install ${APPNAME}; \
	elif [ "${args}" -gt 2 ]; then \
		echo "$(ERROR_COLOR)The library name must not contain spaces!$(NO_COLOR)\n"; \
	else \
		echo "$(ERROR_COLOR)Enter the library name!$(NO_COLOR)\n"; \
	fi

push:
	@bash push.sh

req:
	@printf "$(OK_COLOR)==== Install python requirements ====$(NO_COLOR)\n"
	@if [ -d "${VENV}" ]; then \
		$(PIP) install -r requirements.txt; \
	else \
		echo "Environment is absent"; \
		echo "In first run the command:"; \
		echo "make venv"; \
	fi

run:
	@printf "$(OK_COLOR)==== Starting the script ${name} ====$(NO_COLOR)\n"
	@$(eval args := $(words $(filter-out --,$(MAKECMDGOALS))))
	@if [ "${args}" -eq 2 ]; then \
		echo "$(OK_COLOR) Launch script ${APPNAME}$(NO_COLOR)\n"; \
		$(PYTHON) ${APPNAME}; \
	elif [ "${args}" -gt 2 ]; then \
		echo "$(ERROR_COLOR)The script name must not contain spaces!$(NO_COLOR)\n"; \
	else \
		echo "$(ERROR_COLOR)Enter the script name!$(NO_COLOR)\n"; \
	fi

venv:
	@printf "$(OK_COLOR)==== Launch virtual environment for ${name} ====$(NO_COLOR)\n"
	@if [ ! -d "${VENV}" ]; then \
        echo "Creating virtual environment..."; \
        python3 -m venv ${VENV}; \
    fi

clean:
	@printf "$(ERROR_COLOR)==== Cleaning cache ${name}... ====$(NO_COLOR)\n"
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr

fclean: clean
	@printf "$(ERROR_COLOR)==== Cleaning configuration ${name}... ====$(NO_COLOR)\n"
	@rm -rf ${VENV}

.PHONY	: all app freeze h help install make migrate req root static venv vexit clean fclean
