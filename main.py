from lib.data_collection import *
from lib.database_conection import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32com.client as win32
from twilio.rest import Client

def main():
    # Open Google Chrome
    driver = webdriver.Chrome()
    driver.get(url="https://www.taquarituba.sp.gov.br/covid")

    # Send e-mails
    emails_do_banco = coletaEmails()
    for endereco in emails_do_banco:
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        email.To = endereco
        email.Subject = "COVID-19 EM TAQUARITUBA"
        email.HTMLBody = f"""
        <h1>LISTA COM OS DADOS DO CORONA VÍRUS EM TAQUARITUBA-SP</h1>
        <p><b>SUSPEITOS:</b> {suspeitos(driver)} pessoas.</p>
        <p><b>CONFIRMADOS:</b> {confirmados(driver)} pessoas.</p>
        <p><b>DESCARTADOS:</b> {descartados(driver)} pessoas.</p>
        <p><b>CURADOS:</b> {curados(driver)} pessoas.</p>
        <p><b>HOSPITALIZADOS:</b> {hospitalizados(driver)} pessoas.</p>
        <p><b>MORTES:</b> {obitos(driver)} pessoas.</p>
        <p><b>EM ISOLAMENTO:</b> {em_isolamento(driver)} pessoas.</p>
        <br></br>
        {data(driver)}
        """
        email.Send()

    # Close Chrome
    driver.close()
    
    # Send MSM in my phone number
    account_sid = "myaccountnumber"
    auth_token  = "mytokennumber"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="mynumber",
        from_="myaccountnumberphone",
        body="""
        ---------- 
        SAWAN, OS E-MAILS FORAM ENVIADOS COM SUCESSO! 
        ----------
        """)

if __name__ == '__main__':
    main()
