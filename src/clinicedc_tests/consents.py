from dateutil.relativedelta import relativedelta
from edc_consent.consent_definition import ConsentDefinition

# default consent definition for most tests
consent_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv1",
    gender=["M", "F"],
    version="1",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)

consent1_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv1",
    end_rdelta=relativedelta(days=50),
    gender=["M", "F"],
    version="1.0",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)


consent1_v2 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv2",
    start_rdelta=relativedelta(days=51),
    end_rdelta=relativedelta(days=100),
    gender=["M", "F"],
    version="2.0",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)

consent1_v3 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv3",
    start_rdelta=relativedelta(days=101),
    end_rdelta=relativedelta(days=200),
    gender=["M", "F"],
    version="3.0",
    age_min=16,
    age_max=64,
    age_is_adult=18,
    updates=consent1_v2,
)


consent2_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsent2v1",
    start_rdelta=relativedelta(days=31),
    gender=["M", "F"],
    version="2.1",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)

consent2_v2 = ConsentDefinition(
    "clinicedc_tests.subjectconsent2v2",
    start_rdelta=relativedelta(days=75),
    gender=["M", "F"],
    version="2.2",
    age_min=16,
    age_max=64,
    age_is_adult=18,
    updates=consent2_v1,
)

consent5_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv5",
    gender=["M", "F"],
    version="5",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)

consent6_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv6",
    gender=["M", "F"],
    version="6",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)

consent7_v1 = ConsentDefinition(
    "clinicedc_tests.subjectconsentv7",
    gender=["M", "F"],
    version="7",
    age_min=16,
    age_max=64,
    age_is_adult=18,
)
