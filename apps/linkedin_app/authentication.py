import sys
sys.path.append('C:\\Users\\Josh\\PycharmProjects\\CRM_Project_\\venv\\Lib\\site-packages')

from linkedin_v2.linkedin import (LinkedInAuthentication, LinkedInApplication,
                                  PERMISSIONS)


if __name__ == '__main__':
    API_KEY = '77kt1k9qxz5ru7'
    API_SECRET = 'elDsnOAvPDrrmv9h'
    RETURN_URL = 'http://127.0.0.1:8000/'
    authentication = LinkedInAuthentication(
        API_KEY,
        API_SECRET,
        RETURN_URL,
        PERMISSIONS.enums.values())

    # print(authentication.authorization_url)

    application = LinkedInApplication(token="AQVOKUxTWBO2kM-3eqZodxI5hELSfHMmsW8T9F5Vov2mTrbxmhvAptaF6eCW_CpwzhQpaT20gCLTKH-EwlJsQ1MCT4QStlI3cYDkZmH2DFhFbc7s2gxNxFcaAvHaJpnp42ZTizmqX_3yucNV1YhiHvthUtQiPv1e-ymMwTpIojkGbeb_mGUkgOMQLXoTJjidFzDZ69Kif29taGwwn5LyVrlrki7Tq72pjjYSs8xBoDeKiA1rhlEW6f3t7dMu1giAEj3548fx6jteZdmekA1N6ArPsZllbxcUoL7SCZuyts00XpJY-PlfraKCOHueOuRee13tSH7PAS9yM0C-y-vxRXwIr5pVnQ")

    print(application.get_connections())


