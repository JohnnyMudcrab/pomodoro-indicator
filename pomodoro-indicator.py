#!/usr/bin/env python

import sys
import appindicator
import gtk

PING_FREQUENZY = 60


class Pomodore:
    def __init__(self):
        self.ind = appindicator.Indicator('pomodore-indicator',
                                          '',
                                          appindicator.CATEGORY_OTHER)
        self.ind.set_status(appindicator.STATUS_ACTIVE)

        self.menu_setup()
        self.ind.set_menu(self.menu)
        self.ind.set_label('Pomo')

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem('Quit')
        self.quit_item.connect('activate', self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        gtk.timeout_add(PING_FREQUENZY * 1000, self.run)
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def run(self):
        return True

if __name__ == '__main__':
    indicator = Pomodore()
    indicator.main()
