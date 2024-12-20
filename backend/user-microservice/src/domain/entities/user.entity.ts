import { UserRole } from "../../common/enums/user-role.enum";


export class User {
    constructor(
        public readonly id: number,
        public username: string,
        public password: string,
        public role: UserRole = UserRole.USER,
        public readonly createdAt: Date = new Date(),
        public updatedAt: Date = new Date(),
    ) {}
}
