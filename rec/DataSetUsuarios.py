def usuario():
    usuarios = {"Edney": {"teatro amazonas": 5.0, "porão do alemão": 4.0,"arena da amazônia": 5.0, 
                      "cigs": 5.0,  "cachoeira alto do tarumã": 4.0, "parque cidade da criança": 2.0, 
                      "praça de alimentação do parque 10": 5.0,"bar axerito": 3.0,  "shot in the dark": 5.0},
         
         "Marcus":    {"praia da ponta negra": 5.0, "bosque da ciência": 5.0, "arena da amazônia": 3.0,
                       "amazonas shopping": 4.0,  "praça da saudade": 3.0,"mercado municipal adolpho lisboa": 3.0,
                       "praça de alimentação do parque das laranjeiras": 4.0,"arena paintball": 5.0, "shot in the dark": 4.0},
         
          "Eduardo":    {"bosque da ciência": 5.0, "arena da amazônia": 5.0, "centro cultural dos povos da amazônia": 1.0,
                      "cigs": 5.0, "amazonas shopping": 5.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 4.0,
                      "praça de alimentação do parque 10": 5.0, "praça de alimentação do parque das laranjeiras": 4.0,
                      "bar axerito": 2.0, "arena paintball": 4.0, "shot in the dark": 5.0},
         
          "Patrícia": {"teatro amazonas": 5.0, "praia da ponta negra": 5.0, "porão do alemão": 5.0,
                      "bosque da ciência": 5.0, "arena da amazônia": 3.0, "centro cultural dos povos da amazônia": 5.0,
                      "parque cidade da criança": 5.0, "mercado municipal adolpho lisboa": 3.0,
                      "praça de alimentação do parque 10": 5.0, "praça de alimentação do parque das laranjeiras": 1.0},
         
          "Raissa":    {"praia da ponta negra": 3.0, "porão do alemão": 3.0,"bosque da ciência": 4.0,"cigs": 4.0,
                         "amazonas shopping": 3.0, "cachoeira alto do tarumã": 2.0,"praça de alimentação do parque 10": 4.0,
                        "praça de alimentação do parque das laranjeiras": 4.0,"bar axerito": 4.0},
         
          "Felipe":   { "porão do alemão": 4.0,"bosque da ciência": 5.0, "cigs": 5.0, "amazonas shopping": 5.0,
                        "cachoeira alto do tarumã": 2.0, "praça da saudade": 3.0, "praça de alimentação do parque 10": 4.0,
                        "praça de alimentação do parque das laranjeiras": 4.0, "bar axerito": 4.0, "arena paintball": 5.0, "shot in the dark": 5.0},
         
          "Júlio":    {"amazonas shopping": 3.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 3.0,
                      "parque cidade da criança": 4.0, "mercado municipal adolpho lisboa": 3.0, "praça de alimentação do parque das laranjeiras": 4.0,
                      "bar axerito": 3.0, "shot in the dark": 4.0},
         
          "Karem":    {"teatro amazonas": 5.0, "praia da ponta negra": 4.0,"bosque da ciência": 4.0,
                       "arena da amazônia": 5.0, "centro cultural dos povos da amazônia": 5.0, "cigs": 5.0,
                       "amazonas shopping": 3.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 4.0},
         
         "Mari":    {"parque cidade da criança": 5.0, "mercado municipal adolpho lisboa": 5.0,
                      "praça de alimentação do parque 10": 3.0, "praça de alimentação do parque das laranjeiras": 5.0,
                      "bar axerito": 5.0, "arena paintball": 5.0, "shot in the dark": 4.0},
         
         "Norberto":    {"teatro amazonas": 5.0, "praia da ponta negra": 4.0, "porão do alemão": 4.0,
                      "arena da amazônia": 2.0, "centro cultural dos povos da amazônia": 5.0,
                      "cigs": 5.0, "cachoeira alto do tarumã": 5.0, "praça da saudade": 5.0,
                      "parque cidade da criança": 5.0, "praça de alimentação do parque 10": 5.0,
                         "praça de alimentação do parque das laranjeiras": 5.0, "bar axerito": 5.0, "shot in the dark": 5.0},
         
         "Neila":    {"teatro amazonas": 5.0,"porão do alemão": 5.0,"bosque da ciência": 5.0, "centro cultural dos povos da amazônia": 5.0,
                      "cigs": 5.0, "amazonas shopping": 5.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 1.0,
                      "mercado municipal adolpho lisboa": 4.0,"bar axerito": 5.0, "arena paintball": 5.0, "shot in the dark": 2.0},

         "Heitor":    {"teatro amazonas": 5.0, "praia da ponta negra": 4.0,"bosque da ciência": 3.0, "arena da amazônia": 5.0,
                      "cigs": 5.0, "amazonas shopping": 4.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 4.0,
                      "parque cidade da criança": 3.0, "mercado municipal adolpho lisboa": 2.0,
                      "praça de alimentação do parque 10": 4.0, "praça de alimentação do parque das laranjeiras": 3.0,
                      "bar axerito": 5.0},

         "Anne":    {"teatro amazonas": 2.0, "praia da ponta negra": 4.0, "porão do alemão": 4.0,
                      "bosque da ciência": 5.0, "arena da amazônia": 5.0, "centro cultural dos povos da amazônia": 4.0,
                      "cigs": 5.0, "praça de alimentação do parque 10": 5.0, "praça de alimentação do parque das laranjeiras": 4.0,
                      "bar axerito": 4.0, "arena paintball": 3.0, "shot in the dark": 4.0},

         "José":    {"arena da amazônia": 5.0, "centro cultural dos povos da amazônia": 1.0,
                      "cigs": 3.0, "amazonas shopping": 2.0, "cachoeira alto do tarumã": 4.0, "praça da saudade": 3.0,
                      "parque cidade da criança": 4.0, "mercado municipal adolpho lisboa": 5.0,
                      "praça de alimentação do parque 10": 3.0},

         "Cláudia":    {"teatro amazonas": 1.0, "praia da ponta negra": 3.0, "porão do alemão": 5.0,
                      "bosque da ciência": 5.0},
         
         "Paulo":    {"praça de alimentação do parque 10": 5.0, "praça de alimentação do parque das laranjeiras": 4.0,
                      "bar axerito": 5.0, "arena paintball": 5.0, "shot in the dark": 5.0},

         "André":    {"mercado municipal adolpho lisboa": 3.0, "bar axerito": 5.0, "arena paintball": 4.0, "shot in the dark": 5.0},

         "Luciano":    {"teatro amazonas": 4.0, "praia da ponta negra": 3.0, "porão do alemão": 4.0,
                      "bosque da ciência": 5.0, "arena da amazônia": 5.0, "centro cultural dos povos da amazônia": 5.0,
                      "amazonas shopping": 3.0, "cachoeira alto do tarumã": 5.0, "praça da saudade": 3.0,
                      "mercado municipal adolpho lisboa": 2.0, "praça de alimentação do parque 10": 4.0,
                      "arena paintball": 3.0, "shot in the dark": 4.0},

         "Alecsandro":    {"teatro amazonas": 1.0, "praia da ponta negra": 4.0},

         "Raoni":    {"teatro amazonas": 3.0, "praia da ponta negra": 5.0, "porão do alemão": 5.0,
                      "bosque da ciência": 5.0, "arena da amazônia": 2.0, "centro cultural dos povos da amazônia": 3.0,
                      "amazonas shopping": 5.0, "praça da saudade": 5.0,"parque cidade da criança": 5.0,
                      "mercado municipal adolpho lisboa": 5.0, "praça de alimentação do parque das laranjeiras": 5.0, "arena paintball": 5.0}}

    return usuarios
