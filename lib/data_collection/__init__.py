def suspeitos(driver):
    suspeitos = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[2]/div[1]/div[1]/h3/strong').text
    return suspeitos

def confirmados(driver):
    confirmados = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[2]/div[2]/div[1]/h3/strong').text
    return confirmados

def descartados(driver):
    descartados = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[2]/div[3]/div[1]/h3/strong').text
    return descartados

def curados(driver):
    curados = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[6]/div[1]/div[1]/h3/strong').text
    return curados

def hospitalizados(driver):
    hospitalizados = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[6]/div[2]/div[1]/h3/strong').text
    return hospitalizados

def obitos(driver):
    obitos = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[6]/div[3]/div[1]/h3/strong').text
    return obitos

def em_isolamento(driver):
    em_isolamento = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[3]/div[6]/div[4]/div[1]/h3/strong').text
    return em_isolamento

def data(driver):
    data = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/p').text.replace('ADMSITE', 'SAWAN PEREIRA')
    return data
