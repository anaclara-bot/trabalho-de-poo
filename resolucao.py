medicos = [
    {"nome": "Carlaion",
     "cpf": "758493675845",
     "rg": "MG123456",
     "crm": "CRM1234",
     "telefone": "(88) 99999-1234",
     "endereco": "Rua José Alves Costa, Bairro Juremal, n 278",
     "sexo": "Masculino",
     "senha": "p75t6"},

       {"nome": "Dr. Pedrinho",
     "cpf": "64859256487",
     "rg": "SP987654",
     "crm": "CRM5678",
     "telefone": "(88) 99999-5678",
     "endereco": "Rua Sergio Pontes, Bairro Sanharol, n 187",
     "sexo": "Masculino",
     "senha": "e4w76"}]
pacientes = [
       {"nome": "Ian de morais",
     "cpf": "11557372201",
     "rg": "MG23356",
     "telefone": "(31) 99999-1111",
     "endereco": "Rua Joaquim Gregório, 721, Bahia",
     "sexo": "Masculino",
    "convenio": "Convenio Santa Maria" },

       {"nome": "Galego",
     "cpf": "113344556601",
     "rg": "pq33425",
     "telefone": "(11) 33333-2222",
     "endereco": "Avenida Ibicatu, 101, Ceará",
     "sexo": "Masculino",
     "convenio": "Convenio São José"},

       {"nome": "Francisco Adalbs",
     "cpf": "5648769896",
     "rg": "ct5234",
     "telefone": "(11) 55555-2222",
     "endereco": "Avenida Grossos, 105, Ceará",
     "sexo": "Masculino",
     "convenio": "Convenio São José"}]

convenios=[
    {"nome": "convênio Santa Maria",
    "telefone": "(88)3456-3467",
    "endereco": "Rua carlos gonçalves cassundé",
    "cnpj": "239003445",
    "planos": "Plano 2 ,plano 6"},

   {"nome": "Convenio São José",
     "telefone": "(99)28675-5687",
     "endereco": "rua joão alves ferreira, bairro betânia",
     "cnpj": "345099112",
     "planos":"plano 15 , plano 18"}]

consultas = [
    {   "medico": "Dr. Carlaion",
        "paciente":"Ian de morais",
        "data" : "16/07/2024",
        "hora inicial" : "12:00",
        "hora final" : "1:00",
        "descrição" : "consulta de análise ginecológica"},

        {   "medico": "Dr. Pedrinho",
        "paciente":"Galego",
        "data" : "26/03/2024",
        "hora inicial" : "13:00",
        "hora final" : "13:30",
        "descrição" : "Queda de moto"},

        {   "medico": "Dr. Pedrinho",
        "paciente":"Francisco Adalbs",
        "data" : "15/03/2024",
        "hora inicial" : "2:00",
        "hora final" : "3:00",
        "descrição" : "Implante capilar"}]

compromissos = [
{ "data":"30/06/2024",
  "hora inicial":"10:30",
  "hora final":"11:30",
  "descricao":"sessão de fotos", },

{ "data":"12/07/2024",
  "hora inicial":"12::40",
  "hora final":"14;00",
  "descricao":"exame", }]



from datetime import datetime
import re

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def cadastrarMedicos():
    NOMEMEDI = input("digite o nome do medico")
    IDADEMEDI =input("digite a idade do medico ")
    CPFMEDI = input("digite o cpf do medico ")
    RGMEDI = input("digite o rg do medico ") 
    CRMMEDI = input("digite o crm do medico")
    TELEFONEMEDI =input("digite o telefone do medico")
    ENDERECOMEDI = input("digite o endereço do medico")
    SEXOMEDI = input("digite o sexo do medico")
    SENHAMEDI = ("digite a senha do medico")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("Seu dados foram cadastrados!")
        medicos.append({"nome":NOMEMEDI,
                "idade":IDADEMEDI,
                "cpf": CPFMEDI,
                "rg":RGMEDI,
                "crm":CRMMEDI,
                "telefone":TELEFONEMEDI,
                "endereço":ENDERECOMEDI,
                "sexo":SEXOMEDI,
                "senha":SENHAMEDI })
        print(medicos)
    else:
        print("programa cancelado!")
        breakpoint
    

def cadastrarPacientes():
    NOMEPACI = input("Digite o nome do paciente: ")
    CPFPACI = input("Digite o CPF do paciente: ")
    RGPACI = input("Digite o RG do paciente: ")
    TELEFONEPACI = input("Digite o telefone do paciente: ")
    ENDERECOPACI = input("Digite o endereço do paciente: ")
    SEXOPACI = input("Digite o sexo do paciente (M/F): ")
    CONVENIOPACI = input("Digite o convenio que o paciente está associado: ")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("Seus dados foram cadastrados!")
        pacientes.append({"nome":NOMEPACI,
                "cpf": CPFPACI,
                "rg":RGPACI,
                "telefone":TELEFONEPACI,
                "endereço":ENDERECOPACI,
                "sexo":SEXOPACI,
                "convenio":CONVENIOPACI })
        print(pacientes)
    else:
        print("progra1ma cancelado!")
        breakpoint

def cadastrarConvenios():
    NOMECONV=input("digite o seu nome:")
    TELEFONECONV=input("digite seu telefone para contato:")
    ENDERECOCONV=input("digite seu endereço:")
    CNPJCONV=input("digite seu cnpj:")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("Seus dados foram cadastrados!")
        convenios.append({"nome":NOMECONV,
                "telefone":TELEFONECONV,
                "endereço":ENDERECOCONV,
                "cnpj":CNPJCONV})
        print(convenios)
    else:
        print("programa cancelado!")
        breakpoint

def buscarMedicos():
    print("Informe o nome ou CRM do médico que deseja buscar:")
    busm = input("")
    resultados = [medico for medico in medicos if busm.lower() == medico.get('nome', '').lower() or busm == medico.get('crm', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")

def buscarPacientes():
    print("Informe o nome ou CPF do paciente que deseja buscar:")
    busp = input("")
    resultados = [paciente for paciente in pacientes if busp.lower() == paciente.get('nome', '').lower() or busp == paciente.get('cpf', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")

def buscarConvenios():
    print("Informe o nome ou CNPJ do convênio que deseja buscar:")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc.lower() == convenio.get('nome', '').lower() or busc == convenio.get('cnpj', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
    else:
        print("Nenhum convênio encontrado.")

def alterarMedicos():
  
  print("Informe o CRM do médico que deseja alterar:")
  crm = input("")
  medico = next((medico for medico in medicos if medico['crm'] == crm), None)
  if medico:
        print(f"Dados atuais: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
        cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
        rg = input(f"RG ({medico['rg']}): ") or medico['rg']
        telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
        endereco = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
        sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
        senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        medico.update({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "senha": senha
        })
        print("Dados do médico atualizados.")
        print(medicos)
  else:
        print("Médico não encontrado.")

def alterarPacientes():

    print("Informe o CPF do paciente que deseja alterar:")
    cpf = input("")
    paciente = next((paciente for paciente in pacientes if paciente['cpf'] == cpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
        paciente.update({
            "nome": nome,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
        })
        print("Dados do paciente atualizados.")
    else:
        print("Paciente não encontrado.")
    
def marcarCompromisso():
    print("Você deseja marcar um compromisso? Digite: SIM ou NÃO.")
    com = input("")
    if com.upper() == "SIM":
        data = input("Qual a data do compromisso que deseja marcar? ex: 07/06/2024: ")
        if not validar_data(data):
            print("Data inválida. Encerrando o programa.")
            return
        
        hinicial = input("Informe a hora inicial do compromisso (formato HH:MM): ")
        hfinal = input("Informe a hora final do compromisso (formato HH:MM): ")
        descricao = input("Descreva qual o seu compromisso: ")
        
        compromissos.append({
            "data": data,
            "hora inicial": hinicial,
            "hora final": hfinal,
            "descrição": descricao
        })
        print("Compromisso marcado com sucesso!")
        print(f"Seu compromisso foi agendado com os seguintes dados: {compromissos[-1]}")
    else:
        print("Programa cancelado!")

def marcarConsulta():
    print("Você quer marcar uma consulta? (SIM/NÃO): ")
    mc = input("")
    if mc.upper() == "SIM":
        nm = input("Qual médico você deseja se consultar? ")
        mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
        if mencontrado:
            pnome = input("Informe o nome do paciente: ")
            pencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pnome), None)
            if pencontrado:
                data = input("Informe a data da consulta (formato DD/MM/AAAA): ")
                if not validar_data(data):
                    print("Data inválida. Encerrando o programa.")
                    return
                
                hinicial = input("Informe a hora inicial da consulta (formato HH:MM): ")
                hfinal = input("Informe a hora final da consulta (formato HH:MM): ")
                descricao = input("Descreva a consulta: ")
                
                consultas.append({
                    "data": data,
                    "hora inicial": hinicial,
                    "hora final": hfinal,
                    "medico": nm,
                    "paciente": pnome,
                    "descrição": descricao
                })
                print("Consulta marcada com sucesso!")
                print(f"Os dados da consulta são: {consultas[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")
    else:
        print("Programa cancelado!")

def emitirRelatorio():
    print("Qual relatório você deseja emitir? ")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    print("5 - Compromissos realizados em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados: " )
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['cnpj']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Encerrando o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Encerrando o programa.")
            return
        
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in consultas:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta['hora inicial']}-{consulta['hora final']}, Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Descrição: {consulta['descrição']}")
    elif escolha == "5":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Por favor reinicie o encerre o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Por favor reinicie o encerre o programa.")
            return
        
        print(f"Compromissos de {data_inicio} a {data_fim}:")
        for compromisso in compromissos:
            data_compromisso = compromisso.get("data", "")
            if data_inicio <= data_compromisso <= data_fim:
                print(f"Data: {compromisso['data']}, Horário: {compromisso['hora inicial']}-{compromisso['hora final']}, Descrição: {compromisso['descrição']}")
    else:
        print("Opção inválida. Encerrando o programa.")
a = True
while a:
   
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")


   match lang:
       case "1":
            cadastrarMedicos()
            
       case "2":
           cadastrarPacientes()
           
       case "3":
           cadastrarConvenios()
       
       case "4":
           buscarMedicos()
   
       case "5":
           buscarPacientes()
           
       case "6":
           buscarConvenios()
   
       case "7":
           alterarMedicos()
   
       case "8":
           alterarPacientes()
       
       case "9":
           marcarCompromisso()
   
       case "10":
           marcarConsulta()
   
       case "11":
           emitirRelatorio()
       
       case "12":
           print("Programa Encerrado!")
           breakpoint
   
       case _:
           print("Escolha uma opção válida")
           lang = input("O que você deseja fazer? \n"
               "1 - Cadastrar Médicos\n"
                "2 - Cadastrar Pacientes\n"
                "3 - Cadastrar Convênios\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer? ")
   