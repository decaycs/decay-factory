PREFIX = /usr

all:
	@echo Run \'make install\' to install odf.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p odf.sh $(DESTDIR)$(PREFIX)/bin/odf
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/odf
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/odfpy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/odfpy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/odf
	@rm -rf $(DESTDIR)$(PREFIX)/bin/odfpy
