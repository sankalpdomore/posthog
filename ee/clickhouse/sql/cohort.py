CALCULATE_COHORT_PEOPLE_SQL = """
SELECT distinct_id FROM ({latest_distinct_id_sql}) where {query} AND team_id = %(team_id)s
"""
