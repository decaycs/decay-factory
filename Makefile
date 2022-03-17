PREFIX = /usr

all:
	@echo Run \'make install\' to install catFactory.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p cat.sh $(DESTDIR)$(PREFIX)/bin/catFactory
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/catFactory
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/catFactorypy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/catFactorypy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/catFactory
	@rm -rf $(DESTDIR)$(PREFIX)/bin/catFactory
