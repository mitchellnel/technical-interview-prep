from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merged = []

        # build up a graph
        # emails to accounts
        emails_to_accounts = {}
        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email not in emails_to_accounts:
                    emails_to_accounts[email] = []

                emails_to_accounts[email].append(i)

        # dfs on each account to look for connected emails
        visited_accounts = [False for _ in range(len(accounts))]

        def dfs(i, emails_set):
            if visited_accounts[i]:
                return

            visited_accounts[i] = True

            emails = accounts[i][1:]
            for email in emails:
                emails_set.add(email)

                for neighbour in emails_to_accounts[email]:
                    dfs(neighbour, emails_set)

        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue

            name, emails = account[0], set()
            dfs(i, emails)

            merged.append([name] + list(sorted(emails)))

        return merged


def main():
    soln = Solution()

    print(
        f'Merging [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
    )
    print(
        f'\t--> {soln.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])}'
    )

    print(
        f'Merging [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]'
    )
    print(
        f'\t--> {soln.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]])}'
    )


main()
