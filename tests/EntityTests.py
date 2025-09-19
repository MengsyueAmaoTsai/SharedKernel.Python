from richillcapital_shared_kernel import Entity, IDomainEvent, SingleValueObject


class TestEntityId(SingleValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value)


class TestEntity(Entity[TestEntityId]):
    def __init__(self, id: TestEntityId, name: str) -> None:
        super().__init__(id)
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


class TestDomainEvent(IDomainEvent):
    pass


class EntityTests:
    def test_raise_domain_event_should_add_domain_event(self) -> None:
        entityId = TestEntityId("123")
        entity = TestEntity(entityId, "TestEntity")
        event = TestDomainEvent()
        entity.raise_domain_event(event)

        domainEvents = list(entity.get_domain_events())

        assert event in domainEvents

    def test_clear_domain_events_should_remove_domain_events(self) -> None:
        entityId = TestEntityId("123")
        entity = TestEntity(entityId, "TestEntity")
        event = TestDomainEvent()
        entity.raise_domain_event(event)

        entity.clear_domain_events()

        domainEvents = list(entity.get_domain_events())

        assert len(domainEvents) == 0

    def test_equals_operator_with_same_id_should_be_equal(self) -> None:
        entityId = TestEntityId("123")
        entity1 = TestEntity(entityId, "TestEntity")
        entity2 = TestEntity(entityId, "TestEntity")

        assert (entity1 == entity2) is True

    def test_equals_operator_with_different_id_should_not_be_equal(self) -> None:
        entityId1 = TestEntityId("123")
        entityId2 = TestEntityId("456")
        entity1 = TestEntity(entityId1, "TestEntity")
        entity2 = TestEntity(entityId2, "TestEntity")

        assert (entity1 == entity2) is False

    def test_not_equals_operator_with_same_id_should_not_be_equal(self) -> None:
        entityId = TestEntityId("123")
        entity1 = TestEntity(entityId, "TestEntity")
        entity2 = TestEntity(entityId, "TestEntity")

        assert (entity1 != entity2) is False

    def test_not_equals_operator_with_different_id_should_be_equal(self) -> None:
        entityId1 = TestEntityId("123")
        entityId2 = TestEntityId("456")
        entity1 = TestEntity(entityId1, "TestEntity")
        entity2 = TestEntity(entityId2, "TestEntity")

        assert (entity1 != entity2) is True

    def test_get_hash_code_entities_with_same_id_should_return_same_hash_code(
        self,
    ) -> None:
        entityId = TestEntityId("123")
        entity1 = TestEntity(entityId, "TestEntity")
        entity2 = TestEntity(entityId, "TestEntity")

        assert hash(entity1) == hash(entity2)

    def test_get_hash_code_entities_with_different_id_should_return_different_hash_code(
        self,
    ) -> None:
        entityId1 = TestEntityId("123")
        entityId2 = TestEntityId("456")
        entity1 = TestEntity(entityId1, "TestEntity")
        entity2 = TestEntity(entityId2, "TestEntity")

        assert hash(entity1) != hash(entity2)
