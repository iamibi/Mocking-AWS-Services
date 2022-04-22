from boto3.dynamodb.conditions import Key
import boto3


class Service:
    __dynamodb = None
    __table = None

    def __init__(self, table_name: str, env="dev") -> None:
        """
        Initiates an object of this class

        :param table_name: The table this service is going to perform CRUD operations for.
        :param env: The environment context the application is running in.
        """

        # Create a boto3 resource for local instance of dynamodb
        resource = {"region_name": "us-east-2"}
        if env == "dev":
            resource["endpoint_url"] = "http://localhost:8000"
        self.__dynamodb = boto3.resource("dynamodb", **resource)

        # Get the table
        self.get_table(table_name)

    def get_table(self, table_name: str):
        # Get the table from the dynamodb instance
        self.__table = self.__dynamodb.Table(table_name)

        try:
            # Check whether the table exists or not
            self.__table.table_status
        except:
            # If the table doesn't exist, an exception will be thrown.
            # Create the table if that happens.
            print("The table user doesn't exist. Creating now...")
            self.create_table(table_name)

    def create_table(self, table_name: str):
        try:
            table = self.__dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {"AttributeName": "username", "KeyType": "HASH"},
                    {"AttributeName": "age", "KeyType": "RANGE"},
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "username",
                        "AttributeType": "S",
                    },
                    {
                        "AttributeName": "age",
                        "AttributeType": "N",
                    },
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                },
            )

            # Wait until the table exits
            table.wait_until_exists()
        except Exception:
            raise Exception(f"Unable to create the table {table_name}")

        # Set the instance variable to the new table created
        self.__table = table

    def delete_table(self):
        self.__table.delete()

    def create_user(self, username: str, email: str, age: int, first_name: str, last_name: str):
        user_obj = {
            "username": username,
            "email": email,
            "age": age,
            "first_name": first_name,
            "last_name": last_name
        }

        # Insert the data into table
        self.__table.put_item(Item=user_obj)

    def get_user_by_username(self, username: str):
        response = self.__table.query(
            KeyConditionExpression=Key("username").eq(username)
        )
        items = response["Items"]

        # Return none, if the length of the items list is not 1
        if len(items) != 1:
            return None

        # Return the value fetched from the database
        return items[0]

    def delete_user_by_username(self, username: str):
        response = self.__table.delete_item(
            Key={"username": username}
        )

        return response
