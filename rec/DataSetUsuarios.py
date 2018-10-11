def usuario():
    usuarios = {"Edney": {"Teatro Amazonas": 5.0, "Porão do Alemão": 4.0,"Arena da Amazonia": 5.0, 
                      "CIGS": 5.0,  "Cachoeira Alto do Tarumã": 4.0, "Parque Cidade da Criança": 2.0, 
                      "Praça de Alimentação do Parque 10": 5.0,"Bar Axerito": 3.0,  "Shot in the Dark": 5.0},
         
         "Marcus":    {"Praia da Ponta Negra": 5.0, "Bosque da Ciência": 5.0, "Arena da Amazonia": 3.0,
                       "Amazonas Shopping": 4.0,  "Praça da Saudade": 3.0,"Mercado Municipal Adolpho Lisboa": 3.0,
                       "Praça de Alimentação do Parque das Laranjeiras": 4.0,"Arena Paintball": 5.0, "Shot in the Dark": 4.0},
         
          "Eduardo":    {"Bosque da Ciência": 5.0, "Arena da Amazonia": 5.0, "Centro Cultural dos Povos da Amazônia": 1.0,
                      "CIGS": 5.0, "Amazonas Shopping": 5.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 4.0,
                      "Praça de Alimentação do Parque 10": 5.0, "Praça de Alimentação do Parque das Laranjeiras": 4.0,
                      "Bar Axerito": 2.0, "Arena Paintball": 4.0, "Shot in the Dark": 5.0},
         
          "Patrícia": {"Teatro Amazonas": 5.0, "Praia da Ponta Negra": 5.0, "Porão do Alemão": 5.0,
                      "Bosque da Ciência": 5.0, "Arena da Amazonia": 3.0, "Centro Cultural dos Povos da Amazônia": 5.0,
                      "Parque Cidade da Criança": 5.0, "Mercado Municipal Adolpho Lisboa": 3.0,
                      "Praça de Alimentação do Parque 10": 5.0, "Praça de Alimentação do Parque das Laranjeiras": 1.0},
         
          "Raissa":    {"Praia da Ponta Negra": 3.0, "Porão do Alemão": 3.0,"Bosque da Ciência": 4.0,"CIGS": 4.0,
                         "Amazonas Shopping": 3.0, "Cachoeira Alto do Tarumã": 2.0,"Praça de Alimentação do Parque 10": 4.0,
                        "Praça de Alimentação do Parque das Laranjeiras": 4.0,"Bar Axerito": 4.0},
         
          "Felipe":   { "Porão do Alemão": 4.0,"Bosque da Ciência": 5.0, "CIGS": 5.0, "Amazonas Shopping": 5.0,
                        "Cachoeira Alto do Tarumã": 2.0, "Praça da Saudade": 3.0, "Praça de Alimentação do Parque 10": 4.0,
                        "Praça de Alimentação do Parque das Laranjeiras": 4.0, "Bar Axerito": 4.0, "Arena Paintball": 5.0, "Shot in the Dark": 5.0},
         
          "Júlio":    {"Amazonas Shopping": 3.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 3.0,
                      "Parque Cidade da Criança": 4.0, "Mercado Municipal Adolpho Lisboa": 3.0, "Praça de Alimentação do Parque das Laranjeiras": 4.0,
                      "Bar Axerito": 3.0, "Shot in the Dark": 4.0},
         
          "Karem":    {"Teatro Amazonas": 5.0, "Praia da Ponta Negra": 4.0,"Bosque da Ciência": 4.0,
                       "Arena da Amazonia": 5.0, "Centro Cultural dos Povos da Amazônia": 5.0, "CIGS": 5.0,
                       "Amazonas Shopping": 3.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 4.0},
         
         "Mari":    {"Parque Cidade da Criança": 5.0, "Mercado Municipal Adolpho Lisboa": 5.0,
                      "Praça de Alimentação do Parque 10": 3.0, "Praça de Alimentação do Parque das Laranjeiras": 5.0,
                      "Bar Axerito": 5.0, "Arena Paintball": 5.0, "Shot in the Dark": 4.0},
         
         "Norberto":    {"Teatro Amazonas": 5.0, "Praia da Ponta Negra": 4.0, "Porão do Alemão": 4.0,
                      "Arena da Amazonia": 2.0, "Centro Cultural dos Povos da Amazônia": 5.0,
                      "CIGS": 5.0, "Cachoeira Alto do Tarumã": 5.0, "Praça da Saudade": 5.0,
                      "Parque Cidade da Criança": 5.0, "Praça de Alimentação do Parque 10": 5.0,
                         "Praça de Alimentação do Parque das Laranjeiras": 5.0, "Bar Axerito": 5.0, "Shot in the Dark": 5.0},
         
         "Neila":    {"Teatro Amazonas": 5.0,"Porão do Alemão": 5.0,"Bosque da Ciência": 5.0, "Centro Cultural dos Povos da Amazônia": 5.0,
                      "CIGS": 5.0, "Amazonas Shopping": 5.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 1.0,
                      "Mercado Municipal Adolpho Lisboa": 4.0,"Bar Axerito": 5.0, "Arena Paintball": 5.0, "Shot in the Dark": 2.0},

         "Heitor":    {"Teatro Amazonas": 5.0, "Praia da Ponta Negra": 4.0,"Bosque da Ciência": 3.0, "Arena da Amazonia": 5.0,
                      "CIGS": 5.0, "Amazonas Shopping": 4.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 4.0,
                      "Parque Cidade da Criança": 3.0, "Mercado Municipal Adolpho Lisboa": 2.0,
                      "Praça de Alimentação do Parque 10": 4.0, "Praça de Alimentação do Parque das Laranjeiras": 3.0,
                      "Bar Axerito": 5.0},

         "Anne":    {"Teatro Amazonas": 2.0, "Praia da Ponta Negra": 4.0, "Porão do Alemão": 4.0,
                      "Bosque da Ciência": 5.0, "Arena da Amazonia": 5.0, "Centro Cultural dos Povos da Amazônia": 4.0,
                      "CIGS": 5.0, "Praça de Alimentação do Parque 10": 5.0, "Praça de Alimentação do Parque das Laranjeiras": 4.0,
                      "Bar Axerito": 4.0, "Arena Paintball": 3.0, "Shot in the Dark": 4.0},

         "José":    {"Arena da Amazonia": 5.0, "Centro Cultural dos Povos da Amazônia": 1.0,
                      "CIGS": 3.0, "Amazonas Shopping": 2.0, "Cachoeira Alto do Tarumã": 4.0, "Praça da Saudade": 3.0,
                      "Parque Cidade da Criança": 4.0, "Mercado Municipal Adolpho Lisboa": 5.0,
                      "Praça de Alimentação do Parque 10": 3.0},

         "Cláudia":    {"Teatro Amazonas": 1.0, "Praia da Ponta Negra": 3.0, "Porão do Alemão": 5.0,
                      "Bosque da Ciência": 5.0},
         
         "Paulo":    {"Praça de Alimentação do Parque 10": 5.0, "Praça de Alimentação do Parque das Laranjeiras": 4.0,
                      "Bar Axerito": 5.0, "Arena Paintball": 5.0, "Shot in the Dark": 5.0},

         "André":    {"Mercado Municipal Adolpho Lisboa": 3.0, "Bar Axerito": 5.0, "Arena Paintball": 4.0, "Shot in the Dark": 5.0},

         "Luciano":    {"Teatro Amazonas": 4.0, "Praia da Ponta Negra": 3.0, "Porão do Alemão": 4.0,
                      "Bosque da Ciência": 5.0, "Arena da Amazonia": 5.0, "Centro Cultural dos Povos da Amazônia": 5.0,
                      "Amazonas Shopping": 3.0, "Cachoeira Alto do Tarumã": 5.0, "Praça da Saudade": 3.0,
                      "Mercado Municipal Adolpho Lisboa": 2.0, "Praça de Alimentação do Parque 10": 4.0,
                      "Arena Paintball": 3.0, "Shot in the Dark": 4.0},

         "Alecsandro":    {"Teatro Amazonas": 1.0, "Praia da Ponta Negra": 4.0},

         "Raoni":    {"Teatro Amazonas": 3.0, "Praia da Ponta Negra": 5.0, "Porão do Alemão": 5.0,
                      "Bosque da Ciência": 5.0, "Arena da Amazonia": 2.0, "Centro Cultural dos Povos da Amazônia": 3.0,
                      "Amazonas Shopping": 5.0, "Praça da Saudade": 5.0,"Parque Cidade da Criança": 5.0,
                      "Mercado Municipal Adolpho Lisboa": 5.0, "Praça de Alimentação do Parque das Laranjeiras": 5.0, "Arena Paintball": 5.0}}

    return usuarios
