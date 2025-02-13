from ..models import User
import os

NAIVE_PASSWORD = os.getenv("SEED_USER_PWD", "password")

#                 User, password
USER_SEEDS: list[tuple[User, str]] = [
    (
        User(
            id=1_001_000,
            username="admin",
            first_name="Adam",
            last_name="Administrator",
            email="admin@shelter.cz",
            contact_info="+420-955-123-456",
            role=User.Role.ADMINISTRATOR,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_001,
            username="michael",
            first_name="Michael",
            last_name="Wee",
            email="wee@gmail.com",
            contact_info="0907000001",
            role=User.Role.ADMINISTRATOR,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_002,
            username="tampol",
            first_name="Tamara",
            last_name="Pollar",
            email="dui.fusce@aol.ca",
            contact_info="1-634-667-2515",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_003,
            username="harvey",
            first_name="Upton",
            last_name="Harvey",
            email="sed.molestie@google.net",
            contact_info="214-7437",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_004,
            username="blakeRae",
            first_name="Rae",
            last_name="Blake",
            email="sed@outlook.edu",
            contact_info="321-3272",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_005,
            username="jesse_hubbard",
            first_name="Jesse",
            last_name="Hubbard",
            email="lacus@protonmail.ca",
            contact_info="1-625-851-9642",
            role=User.Role.UNVERIFIED,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_006,
            username="evelyn_zimmerman",
            first_name="Evelyn",
            last_name="Zimmerman",
            email="et.ultrices@yahoo.couk",
            contact_info="1-661-428-6255",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_007,
            username="tiger_king",
            first_name="Tiger",
            last_name="King",
            email="nunc.mauris@hotmail.edu",
            contact_info="(445) 898-2903",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_008,
            username="willow_jones",
            first_name="Willow",
            last_name="Jones",
            email="ipsum@protonmail.couk",
            contact_info="(455) 731-1633",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_009,
            username="ezekiel_leach",
            first_name="Ezekiel",
            last_name="Leach",
            email="etiam.imperdiet.dictum@icloud.couk",
            contact_info="(744) 268-5624",
            role=User.Role.UNVERIFIED,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_010,
            username="nayda_moses",
            first_name="Nayda",
            last_name="Moses",
            email="erat@yahoo.com",
            contact_info="1-485-250-1298",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_011,
            username="liberty_macias",
            first_name="Liberty",
            last_name="Macias",
            email="iaculis@hotmail.couk",
            contact_info="(319) 975-7417",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_012,
            username="althea_hays",
            first_name="Althea",
            last_name="Hays",
            email="id.risus.quis@aol.org",
            contact_info="(788) 864-7477",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_013,
            username="tatum_beasley",
            first_name="Tatum",
            last_name="Beasley",
            email="in@hotmail.edu",
            contact_info="(375) 381-6152",
            role=User.Role.ADMINISTRATOR,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_014,
            username="priscilla_barnes",
            first_name="Priscilla",
            last_name="Barnes",
            email="vel.pede@icloud.org",
            contact_info="(341) 122-7770",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_015,
            username="slade_lewis",
            first_name="Slade",
            last_name="Lewis",
            email="netus.et.malesuada@yahoo.net",
            contact_info="(828) 611-6565",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_016,
            username="catherine_logan",
            first_name="Catherine",
            last_name="Logan",
            email="turpis.vitae@aol.ca",
            contact_info="(184) 338-6638",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_017,
            username="keiko_williams",
            first_name="Keiko",
            last_name="Williams",
            email="pharetra@icloud.edu",
            contact_info="1-305-834-3008",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_018,
            username="tucker_webster",
            first_name="Tucker",
            last_name="Webster",
            email="amet.ultricies@icloud.com",
            contact_info="1-628-822-6868",
            role=User.Role.CAREGIVER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_019,
            username="neil_fox",
            first_name="Neil",
            last_name="Fox",
            email="sed.orci@icloud.com",
            contact_info="(553) 149-1764",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_020,
            username="randall_deleon",
            first_name="Randall",
            last_name="Deleon",
            email="laoreet.lectus@aol.couk",
            contact_info="1-736-269-3245",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_021,
            username="james_sharpe",
            first_name="James",
            last_name="Sharpe",
            email="tincidunt.aliquam@icloud.org",
            contact_info="1-518-728-1192",
            role=User.Role.UNVERIFIED,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_022,
            username="amity_dudley",
            first_name="Amity",
            last_name="Dudley",
            email="fermentum.risus@aol.couk",
            contact_info="1-272-617-8067",
            role=User.Role.UNVERIFIED,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_023,
            username="beck_reeves",
            first_name="Beck",
            last_name="Reeves",
            email="ultricies@outlook.com",
            contact_info="1-774-773-2485",
            role=User.Role.VETERINARIAN,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_024,
            username="ignatius_lowery",
            first_name="Ignatius",
            last_name="Lowery",
            email="duis.at.lacus@aol.couk",
            contact_info="1-256-861-1659",
            role=User.Role.VOLUNTEER,
        ),
        NAIVE_PASSWORD,
    ),
    (
        User(
            id=1_001_025,
            username="johnDoe",
            first_name="John",
            last_name="Doe",
            email="jdoe@outlook.edu",
            contact_info="124-77895",
            role=User.Role.VOLUNTEER,
        ),
        "password",
    ),
]
