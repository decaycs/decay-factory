PREFIX = /usr

all:
	@echo Run \'make install\' to install odf.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/odf
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/odf

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/odf
