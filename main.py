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

    # Get the page numbers
    suspects = suspeitos(driver)
    confirmed = confirmados(driver)
    discarded = descartados(driver)
    cured = curados(driver)
    hospitalized = hospitalizados(driver)
    deaths = obitos(driver)
    isolated = isolados(driver)
    date = data(driver)        

    # Close Chrome
    driver.close()

    # Create e-mails list (strong blue text \033[1;34;40)
    emails_do_banco = coletaEmails()
    print(f'\033[1;34mForam encontrados {len(emails_do_banco)} e-mails...\033[m')
    cont = len(emails_do_banco)

    # Send e-mails
    for endereco in emails_do_banco:
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        email.To = endereco
        email.Subject = "COVID-19 EM TAQUARITUBA"
        email.HTMLBody = f"""
        <h1>LISTA COM OS DADOS DO CORONA VÍRUS EM TAQUARITUBA-SP</h1>
        <p><b>SUSPEITOS:</b> {suspects} pessoas.</p>
        <p><b>CONFIRMADOS:</b> {confirmed} pessoas.</p>
        <p><b>DESCARTADOS:</b> {discarded} pessoas.</p>
        <p><b>CURADOS:</b> {cured} pessoas.</p>
        <p><b>HOSPITALIZADOS:</b> {hospitalized} pessoas.</p>
        <p><b>MORTES:</b> {deaths} pessoas.</p>
        <p><b>EM ISOLAMENTO:</b> {isolated} pessoas.</p>
        <br></br>
        {date}
        """
        email.Send()

        # Counter (strong red text \033[1;31)
        print(f'\033[1;31mEnviando os dados para o {cont}º e-mail...\033[m')
        del emails_do_banco(0)
        cont -= 1
    
    # Send MSM in my phone number
    account_sid = "account"
    auth_token  = "token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="mynumber",
        from_="accountnumber",
        body="""
        ----- 
        SAWAN, OS E-MAILS FORAM ENVIADOS COM SUCESSO! 
        -----
        """)

if __name__ == '__main__':
    main()
