import requests,time
from web3.auto import w3
from eth_account.messages import encode_defunct
from eth_account import Account
items = {
    "items": [
        {
            "option": "   10 points",
            "level": "bad"
        },
        {
            "option": "   100 points",
            "level": "good"
        },
        {
            "option": "   300 points",
            "level": "good"
        },
        {
            "option": "   500 points",
            "level": "great"
        },
        {
            "option": "   1000 points",
            "level": "best"
        },
        {
            "option": "   2000 points",
            "level": "best"
        },
        {
            "option": "   +50% points",
            "desc": "multiplier for the next 2 hours",
            "level": "good"
        },
        {
            "option": "   +100% points",
            "desc": "multiplier for the next 2 hours",
            "level": "great"
        },
        {
            "option": "   +200% points",
            "desc": "multiplier for the next 2 hours",
            "level": "best"
        }
    ]
}
# This is an example seed phrase
with open('pl.txt','r')as f:
    r = f.read()
    k = r.split('\n')
while True:
    for private_key in k:
        acct = Account.from_key(private_key)
        address = w3.to_checksum_address(acct.address)
        print(address)
        s = requests.Session()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'dd=imxb5y; intercom-device-id-zw0j0kjp=f5ee6d90-7115-4d6b-849c-ec9610c83ff0; cf_clearance=VseQVaTibWLN90JSuaouVne.XDwsMbY8Kv7RT.u1aKM-1730890977-1.2.1.1-sfh3xUrNoecIZ3onOjDlnCX_aQrBR1l1fXpwgrek0CjX9pAesBJS3gnmDp6yiarG_W836qxtHr1Jnr5yyrhDQO90eNIc3Bnm54dztcZzPeus8QzT.EFkdkWmnXrlvaUFG9lgjBimvO0mgvTdG01b6NH8UisomJdoo4FX.dWj3TjdwvIAH8q8XCbn9nXs2K0tSlsdPnaprH8Nf58t7ZOXnRHVD4LZlHGhqVkg5CiijCXl8EZF3juEEQqFKntoVF5ffc4uCDxJxRsuN5Hk.LvC3z0vtPiDilhRXctcYOrBtEPMTx1eSVE9mXJgdGG7yKRdOuEiAHxB7fYvsa4ohBbamrFZqo.qcxvhtoXjfzXMLvPlL0CghhBq3eKHAqfCY7HL; __Host-next-auth.csrf-token=33b0723439e00a4fb3b89e2e0ab27e757a6fe1b603d4dcbfa0b4525afbdc22fa%7C50ad60c984f1a88faac829547e45c171705be277135768dc64e0117befb04541; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.alphabot.app; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Kk8XEEG16tFJmoui.-37WKuC6drVR8Ed-ndHfWLZj8C3PWtwBwcjFJD-70uy2BFjs1ZXMgVuYp8F10XF3IUBgm-hcl4_vkYNbbRSAKdQIBqHt35UzpXgu69qkYAJ2tcDwpCzfryQNUjflQOZAW-V9X1JeYNDMBjBsBDMLMzwhnvoM5lwGUaox23oQyvXrVQ7qVkVS1f33ALMBVrfegCh_IcNmPtdZJ2yxZReC-CtqU18hNb9gzg2IARvMxKynTxQNHQ2qfp37pAupbZaH0vEkghL35s7ZawUOsm1tD-cVgVcH9s3hXQZBvzMj26WU4NO_EWw7Deyp9FtBNgSraZffmrRZvEmKHcgvAbbXLA.7V7b4txWgmzU3hLIQOjCzg; intercom-session-zw0j0kjp=V1VIZVFCdVR6QjQ0TXdDMlZlNVpJNG9pbTYwQWovUEdLbDFlZzN3a3dBRTMrOEFvTkxiREJjMDNGMEhPSVdlYi0tUHdIcThrRlBCeFEvRS9GVzltWkpQZz09--400802d0c2dd0a790d5fb0e1c881b1cb058104d9',
            'priority': 'u=0, i',
            'referer': 'https://www.alphabot.app/splash',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = s.get('https://www.alphabot.app/boost', headers=headers)
        response = s.get('https://www.alphabot.app/api/auth/session', headers=headers)
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.5',
            # 'cookie': 'dd=q9u0vp; intercom-id-zw0j0kjp=fe64506e-4073-407f-a216-0c373d785e7b; intercom-device-id-zw0j0kjp=823d29b0-70ac-4ab5-818a-b0da845060a4; CookieConsent=true; __Host-next-auth.csrf-token=5c698cb367d7420493d130036d18c462902e32cc07c0d844b6f527132fe8fbc7%7C21d028904e5d78cac86a41b192aaa6107441ba51d05bf6fe892074491dee441b; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.alphabot.app; cf_clearance=0FkfvbpnoHt8FIOBKfWdPQ3AmmMpAGFdSf3DWDsnKEc-1730725120-1.2.1.1-scwB0Se4qrI9Oowlzf8fH.8yq0DvFyM6yfPcFjWfhqOtnfKL1M9ZKq9frkEpPFrxJutU1IypQBqW_YnrlD85i7jvEaYXyCzFXYf179T3K6PSAC_wHJ_RWLjoGckcR_psL52nbyMOn4OFCZEgCVmg9EDZMwZ2mYpMjV6o_gGSshA21uBX9pVvPoynnXWG2GuIXLhApONMDL.jrZ1R6bssN1Kl1lKRHUmKW2dNgTS41ADO8w3l13QYJs98egW2qmEM1cwgwprvxGRSBoaLwaxDwJsSQhwiK6mfBo9O4zBP8wR_2TiLR9HhrcvWKF6j9zFKOHdf7.nrKFDA_TYrHEIKMqI2pbySgtewKR1HEJpBFg2Lny7pJcrWvR6L0rGV0vlB; intercom-session-zw0j0kjp=UUdYYXdlWTBMODhZVWNiSnNIMTJDaUNZbUpIVk9WR1hlNjU5RmpKa2pDakJ5OHZjcmVrRzZJQlNleFV3SUtKMC0tSW5YSlRwRXdUSWRCOEtVSzA0ODRVdz09--4c9f641314f9c2ccc529f3b152f15ffb80cbeec5',
            'if-none-match': 'W/"vs1ldhjvai"',
            'priority': 'u=1, i',
            'referer': 'https://www.alphabot.app/boost',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        params = {
            'address': address,
        }

        response = s.get('https://www.alphabot.app/api/auth/nonce', params=params, headers=headers)
        nonce = response.json()['nonce']

        msg = f'Sign this message to either enter a raffle that requires holding a specific NFT, edit your profile, or to gain access to premium functionality with Alphabot. ({nonce})'
        message = encode_defunct(text=msg)
        signed_message =  w3.eth.account.sign_message(message, private_key=private_key)
        m1 = str(signed_message).split("'))")[0]
        m2 = m1.split("signature=HexBytes('")[1]
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.5',
            'content-type': 'application/json',
            # 'cookie': 'dd=q9u0vp; intercom-id-zw0j0kjp=fe64506e-4073-407f-a216-0c373d785e7b; intercom-device-id-zw0j0kjp=823d29b0-70ac-4ab5-818a-b0da845060a4; CookieConsent=true; __Host-next-auth.csrf-token=5c698cb367d7420493d130036d18c462902e32cc07c0d844b6f527132fe8fbc7%7C21d028904e5d78cac86a41b192aaa6107441ba51d05bf6fe892074491dee441b; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.alphabot.app; cf_clearance=0FkfvbpnoHt8FIOBKfWdPQ3AmmMpAGFdSf3DWDsnKEc-1730725120-1.2.1.1-scwB0Se4qrI9Oowlzf8fH.8yq0DvFyM6yfPcFjWfhqOtnfKL1M9ZKq9frkEpPFrxJutU1IypQBqW_YnrlD85i7jvEaYXyCzFXYf179T3K6PSAC_wHJ_RWLjoGckcR_psL52nbyMOn4OFCZEgCVmg9EDZMwZ2mYpMjV6o_gGSshA21uBX9pVvPoynnXWG2GuIXLhApONMDL.jrZ1R6bssN1Kl1lKRHUmKW2dNgTS41ADO8w3l13QYJs98egW2qmEM1cwgwprvxGRSBoaLwaxDwJsSQhwiK6mfBo9O4zBP8wR_2TiLR9HhrcvWKF6j9zFKOHdf7.nrKFDA_TYrHEIKMqI2pbySgtewKR1HEJpBFg2Lny7pJcrWvR6L0rGV0vlB; intercom-session-zw0j0kjp=UUdYYXdlWTBMODhZVWNiSnNIMTJDaUNZbUpIVk9WR1hlNjU5RmpKa2pDakJ5OHZjcmVrRzZJQlNleFV3SUtKMC0tSW5YSlRwRXdUSWRCOEtVSzA0ODRVdz09--4c9f641314f9c2ccc529f3b152f15ffb80cbeec5; aa=U2FsdGVkX1/QmrUJLbi7YvICJRy5PczxLNqWHL3BnAtoIUPLc2kWkEk3iCMbNfLX',
            'if-none-match': 'W/"q0m8dv67fl28"',
            'priority': 'u=1, i',
            'referer': 'https://www.alphabot.app/boost',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = s.get('https://www.alphabot.app/api/auth/csrf', headers=headers)
        csrf = response.json()['csrfToken']
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'dd=q9u0vp; intercom-id-zw0j0kjp=fe64506e-4073-407f-a216-0c373d785e7b; intercom-device-id-zw0j0kjp=823d29b0-70ac-4ab5-818a-b0da845060a4; CookieConsent=true; cf_clearance=VioI8_cMMahWtFc5Zd8HBaJFzJgM5Rg.yENkDQXYntE-1730774938-1.2.1.1-gV9ePAy9aR5gLdQqhGa38PFB_U8tcyuKyDzBh4wZJKK32CoitbzJwPX3fK1dnN.z.usnAZdsnkG_kVLR5WUr9F8yf4QXzzeK.JBqRSdYzPVKyBCD9kfdYl2Yo1G1LNKRgNY03Jds2I2o.ApSOoGq6OuPtML7_4J1NORFJHjjF7a.lEXEJ7EJ7sSQQt2fZku.miVH0UT6rBXnHkvKmx9Z.mZpIXWHDStuiIYAJBEE2YQW68OQZ.i2kq7YbEzNXi63bHqoIOxyUkMmRqvhRcx4geQDQ1xNUIExQjOoTZc.zWTPnOqXgJMSOnzchUAuBn0xosFBBYLtOQXdutuKFbsXoCNx.OXx_KdKkEJ9dJGi6_p57MY_2yHOYI.8rIuuiX1Z; __Host-next-auth.csrf-token=e2ac33d5c3e29641f18d5574deed02f07290a630374a9d9bc81d2ce87ff54aa5%7C0caed23d83de88d8edba30640749e949c5e1b5a71190095178ae656f6b4f974c; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.alphabot.app%2Fboost%23profile-socials; intercom-session-zw0j0kjp=YmxuTmZPUDQzdzZ0SFJyRUNXS1p1eFErMUtXTjlrYTBHQzRIanhOODRjdm91R2RPZkcwR0dINStQYklmUHh5eS0tbFdqKys3clk2UUV6d3JwczFHeUNyZz09--c26af7033d62b1649a72f21df53ed0c686de76f6; aa=U2FsdGVkX1+W81ZJfzak2FTAI9jdtIybwXNxHRqW1fdjzMRpMlFO5YV3OaAtrvNa',
            'origin': 'https://www.alphabot.app',
            'priority': 'u=1, i',
            'referer': 'https://www.alphabot.app/splash',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            'callbackUrl': 'https://www.alphabot.app/',
            'redirect': 'False',
            'address': address,
            'signature': m2,
            'blockchain': 'ETH',
            'walletType': 'metamask',
            'csrfToken': csrf,
            'json': 'true',
        }

        response = s.post('https://www.alphabot.app/api/auth/callback/credentials', headers=headers, data=data)
        time.sleep(4)
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
            # 'cookie': 'CookieConsent=true; dd=mjr0po; intercom-id-zw0j0kjp=1b1efe8a-46ef-4be3-bff7-2f34dfc39942; intercom-device-id-zw0j0kjp=c1bd3957-20a0-491a-9b96-7408d24438f3; cf_clearance=xemPouPSC11tO7GhRacY.fCJBafD1B8AXtycrZeHFGc-1730775568-1.2.1.1-a7tnhfG3ZChDXgj4CJVt03VNaPEcxq6ZVe.7.5TWxvLXlPprYdYDKbxy3GOMFXHe5ik_hkVYR3llYmDMWrnBr77eH6gybbDJb0UyG4l5vQH3fM..X8m20w9FxlT_Nl.YHyAP14Cc_o5rTF8vPdEy9dyQsCiv9r27S0xbFVXyXeVWxExr874iTlABukI7PT3RcpDioCR3VcTRmvBd2L2Qay.Kr6asJ7e1zMN2Pg0AkEk8coq.JAFNuxYhtztMwat_UkSLIJ78GtMFoaI4pQj8FFUobLhYKHi7GLXPya6JNmx__Z_TKMfLCfeVKVKmzpo2inPt9RHrpn9AVwRuF9zRtIqzdCmC2J6.UW.vM_tpArVPH637WvsKnDnTdBcBdXNG; __Host-next-auth.csrf-token=5e366e3dfe8d1c593a3c7530d77b21281fffa7661a5d8fdf188738781b87ab4f%7C7aa7160fa37db60b8a90762e456671ac376e6909ef46f237dde4d30a346a09b5; _gid=GA1.2.1002449729.1730775568; _gat_UA-228740613-1=1; intercom-session-zw0j0kjp=WldCdU5iM0dqazdlVlVBUHpPL05BVnJ3RmtheHI0ZDhqOWNNK2N3Z3pBaDU4ZVdxTWRESzY0Qzh5R3g3MFc2Ky0tZ1ZaMEg4aGpMWVluQ05Cd3h0MDFaQT09--0b770b890e791a866da94a0e22cb3cb7dd276052; _ga=GA1.2.1362122041.1729777761; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.alphabot.app%2F; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..nkixfqzkvxw4xU_p.ogx_n7PkAMddRpPNXzGkb3tACKFG4R7Ijp0ni3uiykri3x9Y6JCWhsO6YHPYfH_OFGiL0VlfrIKhFX__mwY-pHyXWXvgiXnsM8ntpJnih2ydjF7t7J8CBF10--3UnwNJj1j0GEyCd0h4Gx2ayAaTFfSDtdAhqAx8LBKFCrYT9LqACzr8d637KFXMdRjd1dz2Yy_4UWIYvruV6R5QFW9qbXzxIu1iWB2_j7INvznbpCurmBCKUa_pZ3Eg0jPk5OKkvN8se0CYnrY.hXLh7RHpNkat_-r8wo9YSg; _ga_5P3HN827YC=GS1.1.1730775567.9.1.1730775615.0.0.0',
            'priority': 'u=1, i',
            'referer': 'https://www.alphabot.app/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = s.get('https://www.alphabot.app/api/auth/session', headers=headers)
        id = response.json()['_id']
        print(id)
        response = s.get(f'https://www.alphabot.app/api/platformAirdrops/663c16768d466b80012cb656/points',headers=headers)

        response = s.post(f'https://www.alphabot.app/api/platformAirdrops/663c16768d466b80012cb656/wheel',headers=headers)
        try:
            print(items['items'][response.json()['index']])
        except:
            pass
        time.sleep(10)
    time.sleep(86400)