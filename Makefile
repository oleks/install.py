.PHONY: clean

HEAD_PATH=.git/$(shell cat .git/HEAD | cut -d' ' -f2)

install.py: \
		install.py.m4 \
		LICENSE \
		Makefile \
		$(HEAD_PATH)
	m4 -P -D "HEAD_PATH=$(HEAD_PATH)" $< > $@
	./git-ready-to-deploy.sh

clean:
	rm -f install.py
