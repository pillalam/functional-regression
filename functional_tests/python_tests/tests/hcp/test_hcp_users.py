import os
import base
import random

from utils import hcp_auth
from utils import hcp_users


class TestHcpUsers(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Hcp User tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcpUsers, cls).setUpClass()

        # Target to hcp api
        hcp_auth.connect_target(cls.api_url)

        # Log into hcp using creds
        hcp_auth.login(cls.username, optional_args={'-p=': cls.password})

    def test_hcp_create_user_with_roles(self):
        roles = ['user', 'admin', 'publisher']
        for role in roles:
            # Create user
            name = 'hcp_user' + str(random.randint(1024, 4096))
            password = 'hcp_pwd' + str(random.randint(1024, 4096))
            familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
            givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
            email = 'hcp_user@hpe.com'
            out, err = hcp_users.add_user(
                name, password, familyname, givenname, email,
                optional_args={'--role=': role})
            self.verify('Successfully added user ' + name +
                        ' with role ' + role, out)
            # Connect to hcp with new creds
            out, err = hcp_auth.login(name, optional_args={'-p=': password})
            self.verify('Logged in successfully.', out)

            # Connect to hcp with default creds to delete the updated user
            out, err = hcp_auth.login(self.username,
                                      optional_args={'-p=': self.password})
            self.verify('Logged in successfully.', out)
            # Delete User
            out, err = hcp_users.delete_user(name)
            self.verify('Deleted user ' + name + ' successfully', out)

    def test_hcp_update_user_parameters(self):
        # Create user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        try:
            # Update name parameters for hcp user
            n_familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
            n_givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
            n_email = 'hcp_user_updated@hpe.com'
            optional_args = {'--email=': n_email,
                             '--familyname=': n_familyname,
                             '--givenname=': n_givenname}

            out, err = hcp_users.update_user(name, optional_args=optional_args)
            self.verify('Updated user ' + name + ' successfully', out)
        finally:
            # Connect to hcp with new creds
            out, err = hcp_auth.login(name, optional_args={'-p=': password})
            self.verify('Logged in successfully.', out)

            # Connect to hcp with default creds to delete the updated user
            out, err = hcp_auth.login(self.username,
                                      optional_args={'-p=': self.password})
            self.verify('Logged in successfully.', out)
            # Delete User
            out, err = hcp_users.delete_user(name)
            self.verify('Deleted user ' + name + ' successfully', out)

    def test_hcp_create_update_role(self):
        # Create user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        # Update user
        updated_role = 'admin'
        out, err = hcp_users.update_user(
            name, optional_args={'--newrole=': updated_role})
        self.verify('Updated user ' + name + ' successfully', out)
        # Connect to hcp with new creds
        out, err = hcp_auth.login(name, optional_args={'-p=': password})
        self.verify('Logged in successfully.', out)

        # Connect to hcp with default creds to delete the updated user
        out, err = hcp_auth.login(self.username,
                                  optional_args={'-p=': self.password})
        self.verify('Logged in successfully.', out)
        # Delete User
        out, err = hcp_users.delete_user(name)
        self.verify('Deleted user ' + name + ' successfully', out)

    def test_hcp_update_password_and_check_login(self):
        # Create user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        # Connect to hcp with new creds
        out, err = hcp_auth.login(name, optional_args={'-p=': password})
        self.verify('Logged in successfully.', out)

        # Connect to hcp with default creds to update the new user
        out, err = hcp_auth.login(self.username,
                                  optional_args={'-p=': self.password})
        self.verify('Logged in successfully.', out)

        try:
            # Update user
            updated_password = 'hcp_updated' + str(random.randint(1024, 4096))
            optional_args = {'--newpassword=': updated_password,
                             '--oldpassword=': password}

            out, err = hcp_users.update_user(name,
                                             optional_args=optional_args)
            self.verify('Updated user ' + name + ' successfully', out)
        finally:
            # Connect to hcp with the updated creds
            out, er = hcp_auth.login(name,
                                     optional_args={'-p=': updated_password})
            self.verify('Logged in successfully.', out)

            # Connect to hcp with default creds to delete the updated user
            out, err = hcp_auth.login(self.username,
                                      optional_args={'-p=': self.password})
            self.verify('Logged in successfully.', out)
            # Delete User
            out, err = hcp_users.delete_user(name)
            self.verify('Deleted user ' + name + ' successfully', out)

    def test_hcp_update_invalid_role(self):
        # Create user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        try:
            # Update user
            updated_role = 'newrole'
            out, err = hcp_users.update_user(
                name, optional_args={'--newrole=': updated_role})
            self.verify('Error: Invalid role', err)
        finally:
            # Connect to hcp with default creds to delete the updated user
            out, err = hcp_auth.login(self.username,
                                      optional_args={'-p=': self.password})
            self.verify('Logged in successfully.', out)
            # Delete User
            out, err = hcp_users.delete_user(name)
            self.verify('Deleted user ' + name + ' successfully', out)

    def test_hcp_login_with_non_existing_user(self):
        # Create user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        # Delete User
        out, err = hcp_users.delete_user(name)
        self.verify('Deleted user ' + name + ' successfully', out)
        # Login with non-existing user
        out, err = hcp_auth.login(name,
                                  optional_args={'-p=': password})
        self.verify('Credentials were rejected', err)

    def test_hcp_update_non_existing_user(self):
        # Create and delete hcp user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        # Delete user
        out, err = hcp_users.delete_user(name)
        self.verify('Deleted user ' + name + ' successfully', out)
        updated_role = 'admin'
        out, err = hcp_users.update_user(
            name, optional_args={'--newrole=': updated_role})
        self.verify('Unable to retrieve user: User not found',
                    err)

    def test_hcp_delete_non_existing_user(self):
        # Create and delete hcp user
        name = 'hcp_user' + str(random.randint(1024, 4096))
        password = 'hcp_pwd' + str(random.randint(1024, 4096))
        familyname = 'hcp_family_name' + str(random.randint(1024, 4096))
        givenname = 'hcp_given_name' + str(random.randint(1024, 4096))
        email = 'hcp_user@hpe.com'
        role = 'user'
        out, err = hcp_users.add_user(
            name, password, familyname, givenname, email,
            optional_args={'--role=': role})
        self.verify('Successfully added user ' + name +
                    ' with role ' + role, out)
        # Delete user
        out, err = hcp_users.delete_user(name)
        self.verify('Deleted user ' + name + ' successfully', out)

        # Verify deletion of non-existing user
        out, err = hcp_users.delete_user(name)
        self.verify('Unable to delete user: User not found',
                    err)

if __name__ == '__main__':
    base.unittest.main(verbosity=2)
