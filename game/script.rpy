define minazinha = Character("Doidinha")
define eu = Character("Eu")
define outraMina = Character("Outra Doidinha")

image bgPark = "bgpark.jpg"
image ruas = "ruas.jpg"
image ruasNoite = "ruasnoite.jpg"

image minazinha11 = "minazinha1-1.png"
image outraMina11 = "outraminazinha1-1.png"
image outraMina12 = "outraminazinha1-2.png"
image outraMina13 = "outraminazinha1-3.png"

label start:

    scene bgPark

    show minazinha11
    
    "Você está andando pelo park..."
    "..."
    minazinha "Olá, quem é você?"
    
    eu "Sou o protagonista, e você, quem seria?"
    
    minazinha "Eu tava passando por aqui e vi você ai,"
    minazinha "então eu pensei em te dar um oi."
    
    eu "Ah sim, olá, tudo bem?"
    
    minazinha "Tudo sim, acabei me me mudar pra cá pra cidade e não conheço ninguém"
    
    menu:
        "Quer conhecer um pouco do bairro?":
            jump conhecerBairro
        "Voltar pra casa e chorar porque é um nerd virgem gordo fracassado":    
            jump gameOver
        
    label conhecerBairro:
        
        eu "Quer conhecer um pouco o Bairro?"
        minazinha "Claro!"
        "..."
        minazinha "Para onde iremos?"
        eu "Vareos Places"
        
        scene ruas
        with dissolve
        
        "Andando pelas ruas"
        
        minazinha "Vai demorar muito?"
        
        eu "Já já chegaremos"
        
        "..."
        
        return
    label comerBolachas:
        
        "Tu volta pra casa e o jogo acaba."
        
        return
        
    label gameOver:
        hide minazinha11
        
        scene ruasNoite
        with dissolve
        
        "Voltando para casa outra garota aparece."
        
        show outraMina11
        with dissolve
        
        outraMina "Moço, poderia me ajudar?"
        
        eu "Qual é o problema?"
        
        show outraMina12
        with dissolve
        
        outraMina "O PROBLEMA É..."
        outraMina "V-vo...cê!!"
        
        show outraMina13
        with dissolve
        
        "Você só tá alucinando, gordão!"
    return
