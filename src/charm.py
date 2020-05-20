#!/usr/bin/env python3
import sys
sys.path.append("lib")

import logging

from ops.charm import CharmBase
from ops.framework import Object
from ops.main import main


class FooProvides(Object):

    def __init__(self, charm, relation_name):
        super().__init__(charm, relation_name)

        self.framework.observe(
            charm.on[relation_name].relation_joined,
            self.on_relation_joined
        )

    def on_relation_joined(self, event):
        event.relation.data[self.model.unit]['foo'] = 'bar'


class FooProviderCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)

        self.foo = FooProvides(self, "foo")

        self.framework.observe(self.on.start, self._on_start)
        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        pass

    def _on_start(self, event):
        pass


if __name__ == "__main__":
    main(FooProviderCharm)
