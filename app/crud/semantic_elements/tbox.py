from typedb.api.connection.transaction import TransactionType

from app.db.typedb import get_transaction
from app.models.typedb.semantic_elements import Property


async def create_properties(
    properties: list[Property],
) -> list[Property]:

    definitions = [
        f"attribute {_property.name}, value {_property.value_type.value};"
        for _property in properties
    ]

    query = f"define {' '.join(definitions)}"

    async with get_transaction(
        transaction_type=TransactionType.SCHEMA,
    ) as tx:
        tx.query(query=query).resolve()
        tx.commit()

    return properties


async def create_ontology(
    ontology_name: str,
    properties: list[Property],
) -> str:
    owns_clauses = ", ".join(
        [f"owns {_property.name}" for _property in properties]
    )
    query = f"define entity {ontology_name} {owns_clauses};"

    async with get_transaction(
        transaction_type=TransactionType.SCHEMA,
    ) as tx:
        tx.query(query=query).resolve()
        tx.commit()

    return ontology_name


if __name__ == "__main__":
    import asyncio

    from app.models.typedb.semantic_elements import ValueType

    sample_properties = [
        Property(name="name", value_type=ValueType.STRING),
        Property(name="age", value_type=ValueType.INTEGER),
    ]

    asyncio.run(
        main=create_properties(
            properties=sample_properties,
        )
    )

    asyncio.run(
        main=create_ontology(
            ontology_name="SampleOntology",
            properties=sample_properties,
        )
    )
