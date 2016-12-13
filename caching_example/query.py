import hashlib
from django.db.models.query import QuerySet
from django.core.cache import cache


class CachingQuerySet(QuerySet):

    def iterator(self):
        key = self.generate_querysetkey()
        result_set = cache.get(key)

        if not result_set:
            result_set = list(super(CachingQuerySet, self).iterator())
            cache.set(key, result_set)

        for result in result_set:
            yield result

    def generate_querysetkey(self):
        db_table = self.model._meta.db_table
        sql = self.sql()

        query_key = u'{model}{qs}'.format(
            model=db_table,
            qs=sql)

        key = hashlib.md5(query_key.encode('utf-8')).hexdigest()
        return key

    def sql(self):
        """
        Get sql for the current query.
        """
        clone = self.query.clone()
        sql, params = clone.get_compiler(using=self.db).as_sql()
        return sql % params

