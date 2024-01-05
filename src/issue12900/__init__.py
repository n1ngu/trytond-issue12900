
from trytond.pool import Pool
from trytond.cache import Cache
from trytond.model import Model


class Issue12884(Model):
    "Issue 12884"
    __name__ = "issue12884"
    _some_cache = Cache("sale.line.get_stock_quantity")


def register():
    Pool.register(Issue12884, module="issue12900", type_="model")
