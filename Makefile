PREFIX = /usr

all:
	@echo Run \'make install\' to install decayFactory.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p decay.sh $(DESTDIR)$(PREFIX)/bin/decayFactory
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/decayFactory
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/decayFactorypy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/decayFactorypy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/decayFactory
	@rm -rf $(DESTDIR)$(PREFIX)/bin/decayFactory
