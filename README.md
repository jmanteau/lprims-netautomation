# Cours d'introduction à l'automatisation des réseaux



**Syllabus**

*But*: Donner à l'étudiant un aperçu des technologies utilisées dans le monde des réseaux pour l'automatisation de ceux-ci.

*Niveau*: IUT

*Prérequis*: connaissance de python et des concepts réseaux

Le contenu est structuré de la façon suivante:

* Introduction aux formats de données (comment je stocke la donnée)

* Introduction aux modèles de données et leur transport dans le monde du réseau (comment je structure la donnée et comment je l'achemine)

* Exemple concret des deux points précédents avec OpenConfig

* Présentation d'outils utiles pour l'automatisation du réseau

* TP afin d'utiliser certain des outils présentés

* Les références permettent à l'étudiant intéressé par ce domaine de poursuivre par lui-même.

  ​

## Formats de données
YAML, XML, JSON sont des noms de formats de données texte. Il y a plusieurs choses à comprendre ici:

- Données

  Ca peut être n’importe quoi que vous vouliez sauvegarder ou transmettre : carnet d’adresses, configuration d’un logiciel, contenu d’une base de données, etc. En résumé, tout groupe d’informations que vous souhaitez pouvoir communiquer.

- Format :

  Comment sont organiser ces données. Comme on manipule les données avec un ordinateur, il est nécessaire de les ranger d’une certaine façon. En les rangeant de cette façon, l’ordinateur, si il connait le “format”, est capable d’analyser les données qu’il reçoit. 

- Texte :

  En opposition à “binaire” (ce qui est un abus de langage, puisque du texte en informatique, c’est du binaire). Cela signifie que votre format est organisé autour d’un texte lisible par les humains. 

### XML

**XML** est un langage de **balisage générique** qui permet de **structurer des données** afin qu'elles soient lisibles aussi bien par les humains que par des programmes de toutes sortes. 

**Structure d’un document XML**

* Prologue facultatif (mais recommandé) contenant des déclarations

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
```

* Arbre d’éléments correspondant au contenu du document
    * Chaque élément se compose d’une balise d’ouverture, d’un contenu et d’une
      balise de fermeture
    * Un contenu vide peut se noter `<nomBalise />`
    * Un élément peut porter un ou plusieurs attributs `<nomBalise nomAttribut="valeur"> ... </nomBalise>`
      ou `<nomBalise nomAttribut="valeur"/>`
    * Tout élément fils est complètement inclus dans son élément père
    * Pas de recouvrement entre frères
    * Dans un document il y a un et un seul élément père qui contient tous les
      autres éléments (une seule racine)


* Des commentaires et des instructions de traitement (facultatifs)

```xml
<!-- mon commentaire-->
```
### JSON

JSON (JavaScript Object Notation) utilise la notation des objets JavaScript pour transmettre de l’information structurée. Léger et au format texte, il est dérivé de l’écriture des langages standards de type [ECMAScript](http://www.ecma-international.org/publications/files/ecma-st/ECMA-262.pdf) (norme ISO/IEC 16262). Inscrit au Network Working Group de l’IETF sous la [RFC 4627](http://tools.ietf.org/html/rfc4627). Il est souvent utilisé pour simplifier et alléger les accès à des services web depuis les navigateurs.

Il permet de transmettre tout types de données (tableau, chaine, entier, objet …).

JSON est un format texte complètement indépendant de tout langage, mais les conventions qu'il utilise seront familières à tout programmeur habitué aux langages descendant du C, comme par exemple : C lui-même, C++, C#, Java, JavaScript, Perl, Python et bien d'autres. Ces propriétés font de JSON un langage d'échange de données idéal.

**Syntaxe**

JSON se base sur deux structures :

- Une collection de couples nom/valeur. Divers langages la réifient par un objet, un enregistrement, une structure, un dictionnaire, une table de hachage, une liste typée ou un tableau associatif.
- Une liste de valeurs ordonnées. La plupart des langages la réifient par un tableau, un vecteur, une liste ou une suite

Ces structures de données sont universelles. Pratiquement tous les langages de programmation modernes les proposent sous une forme ou une autre. Il est raisonnable qu'un format de données interchangeable avec des langages de programmation se base aussi sur ces structures.

En JSON, elles prennent les formes suivantes:

Ces mêmes éléments représentent 3 types de données.

- **Objet :**

Un objet est défini par un ensemble d’associations clé/valeur. Il commence par une accolade ouvrante ‘{‘ et se termine par une accolade fermante ‘}’. Chaque nom est suivi de deux-points ‘:’ et les couples nom/valeur sont séparés par des virgules ‘,’.

- **Tableau :**

Un tableau est une collection de valeurs ordonnées. Il commence par un crochet ouvrant ‘[‘ et se termine par un crochet fermant ‘]’. Les valeurs sont séparées par des virgules ‘,’.

- **Valeurs :**

Une valeur peut être soit une chaîne de caractères entre guillemets, soit un nombre, soit true ou false ou null, soit un objet soit un tableau. Ces structures peuvent être imbriquées.
Une chaîne de caractères est une suite de zéro ou plus caractères Unicode, entre guillemets, et utilisant les échappements avec antislash. Un caractère est représenté par une chaîne d’un seul caractère. Une chaîne de caractères est très proche de son équivalent en Java.
Un nombre est très proche de ceux qu’on peut rencontrer en Java, notez toutefois que les formats octal et hexadécimal ne sont pas utilisés.

### YAML

Le nom YAML veut dire “YAML Ain’t Markup Language”, soit “YAML n’est pas un langage de balises”. Si cela met d’emblée des distances avec XML, cela ne nous dit pas ce qu’est YAML. YAML est, [d’après sa spécification](http://yaml.org/spec/1.2/spec.html), un langage de sérialisation de données conçu pour être lisible par des humains et travaillant bien avec les langage de programmation modernes pour les tâches de tous les jours.

```
# Les commentaires sont précédés d'un signe "#", comme cette ligne.

#############
# SCALAIRES #
#############

# Les scalaires sont l'ensemble des types YAML qui ne sont pas des collections
# (listes ou tableaux associatifs).

# Notre objet root (racine), sera une map (carte) et englobera
# l'intégralité du document. Cette map est l'équivalent d'un dictionnaire,
# hash ou objet dans d'autres langages.
clé: valeur
autre_clé: une autre valeur
valeur_numérique: 100
notation_scientifique: 1e+12
booléen: true
valeur_null: null
clé avec espaces: valeur
# Bien qu'il ne soit pas nécessaire de mettre les chaînes de caractères
# entre guillemets, cela reste possible, et parfois utile.
toutefois: "Une chaîne, peut être contenue entre guillemets."
"Une clé entre guillemets.": "Utile si l'on veut utiliser ':' dans la clé."

# Les chaînes couvrant plusieurs lignes, peuvent être écrites au choix,
# comme un "bloc littéral" (avec '|') ou bien un "bloc replié" (avec '>').
bloc_littéral: |
    Tout ce bloc de texte sera la valeur de la clé "bloc_littéral", 
    avec préservation des retours à la ligne.
    Le littéral continue jusqu'à ce que l'indentation soit annulée.
        Toutes lignes qui seraient "davantage indentées" conservent leur
        indentation, constituée de 4 espaces.
bloc_replié: >
    Tout ce bloc de texte sera la valeur de la clé "bloc_replié", mais 
    cette fois-ci, toutes les nouvelles lignes deviendront un simple espace.
    Les lignes vides, comme ci-dessus, seront converties en caractère de
    nouvelle ligne.
        Les lignes "plus-indentées" gardent leurs retours à la ligne -
        ce texte apparaîtra sur deux lignes.
###############
# COLLECTIONS #
###############

# L'imbrication est créée par indentation.
une_map_imbriquée:
    clé: valeur
    autre_clé: autre valeur
    autre_map_imbriquée:
        bonjour: bonjour

# Les clés des maps ne sont pas nécessairement des chaînes de caractères.
0.25: une clé de type flottant

# Les clés peuvent également être des objets s'étendant sur plusieurs lignes,
# en utilisant le signe "?" pour indiquer le début de la clé.
? |
    ceci est une clé
    sur de multiples lignes
: et ceci est sa valeur

# YAML autorise aussi l'usage des collections à l'intérieur des clés,
# mais certains langages de programmation ne le tolère pas si bien.

# Les séquences (équivalent des listes ou tableaux) ressemblent à cela :
une_séquence:
    - Objet 1
    - Objet 2
    - 0.5 # les séquences peuvent contenir des types variés.
    - Objet 4
    - clé: valeur
      autre_clé: autre_valeur
    -
        - Ceci est une séquence
        - dans une autre séquence

# YAML étant un proche parent de JSON, vous pouvez écrire directement
# des maps et séquences façon JSON
json_map: {"clé": "valeur"}
json_seq: [1, 2, 3, "soleil"]

################################
# AUTRES FONCTIONNALITÉES YAML #
################################

# YAML possède une fonctionnalité fort utile nommée "ancres". Celle-ci
# vous permet de dupliquer aisément du contenu au sein de votre document.

# Les deux clés suivantes auront la même valeur :
contenu_ancré: &nom_ancre Cette chaîne sera la valeur des deux clés.
autre_ancre: *nom_ancre

# Avec les tags YAML, vous pouvez explicitement déclarer des types de données.
chaine_explicite: !!str 0.5

# Certains analyseurs syntaxiques (parsers) implémentent des tags spécifiques à
# d'autres langages, comme par exemple celui des nombres complexes de Python.
python_complex_number: !!python/complex 1+2j

#####################
# AUTRES TYPES YAML #
#####################

# YAML interprète également les données formatées ISO de type date et datetime,
# pas seulement les chaînes et nombres.
datetime: 2001-12-15T02:59:43.1Z
datetime_avec_espaces: 2001-12-14 21:59:43.10 -5
date: 2002-12-14

# Le tag !!binary indique que la chaîne à suivre est la représentation binaire
# d'un blob encodé en base64. En clair ? Une image !
fichier_gif: !!binary |
    R0lGODlhDAAMAIQAAP//9/X17unp5WZmZgAAAOfn515eXvPz7Y6OjuDg4J+fn5
    OTk6enp56enmlpaWNjY6Ojo4SEhP/++f/++f/++f/++f/++f/++f/++f/++f/+
    +f/++f/++f/++f/++f/++SH+Dk1hZGUgd2l0aCBHSU1QACwAAAAADAAMAAAFLC
    AgjoEwnuNAFOhpEMTRiggcz4BNJHrv/zCFcLiwMWYNG84BwwEeECcgggoBADs=

# YAML a de même un type "set", semblable à ceci :
set:
    ? item1
    ? item2
    ? item3

# Comme dans Python, les sets ne sont que des maps contenant des valeurs null ;
# le set précédent est l'équivalent du suivant :
set2:
    item1: null
    item2: null
    item3: null
```



### Exemple simple

#### XML

```Xml
<breakfast_menu>
	<food>
		<name>Belgian Waffles</name>
		<price>$5.95</price>
		<description>
Two of our famous Belgian Waffles with plenty of real maple syrup
</description>
		<calories>650</calories>
	</food>
	<food>
		<name>French Toast</name>
		<price>$4.50</price>
		<description>
Thick slices made from our homemade sourdough bread
</description>
		<calories>600</calories>
	</food>
	<food>
		<name>Homestyle Breakfast</name>
		<price>$6.95</price>
		<description>
Two eggs, bacon or sausage, toast, and our ever-popular hash browns
</description>
		<calories>950</calories>
	</food>
</breakfast_menu>
```

#### JSON

```json
{
    "breakfast_menu": {
        "food": [
            {
                "calories": "650",
                "description": "Two of our famous Belgian Waffles with plenty of real maple syrup",
                "name": "Belgian Waffles",
                "price": "$5.95"
            },
            {
                "calories": "600",
                "description": "Thick slices made from our homemade sourdough bread",
                "name": "French Toast",
                "price": "$4.50"
            },
            {
                "calories": "950",
                "description": "Two eggs, bacon or sausage, toast, and our ever-popular hash browns",
                "name": "Homestyle Breakfast",
                "price": "$6.95"
            }
        ]
    }
}
```



#### YAML

```yaml
breakfast_menu:
  food:
  - calories: '650'
    description: Two of our famous Belgian Waffles with plenty of real maple syrup
    name: Belgian Waffles
    price: $5.95
  - calories: '600'
    description: Thick slices made from our homemade sourdough bread
    name: French Toast
    price: $4.50
  - calories: '950'
    description: Two eggs, bacon or sausage, toast, and our ever-popular hash browns
    name: Homestyle Breakfast
    price: $6.95
```



#### Script de conversion

Le script utilisé pour faire cette conversion est [ici](convertdataformat.py).

## Modèles de données et Transport

​		
**Un modèle de données définit explicitement et précisément la structure de données, sa syntaxe et sa sémantique.**

#### Propriétaire / CLI sur SSH

@TODO

#### SNMP / SMI

SNMP est un terme un peu générique qui désigne à la fois un protocole réseau applicatif bien précis, une collection de spécifications pour le management de réseau et la définition de structures de données ainsi que leurs concepts associés.

SNMP est né en 1988 de la nécessité de disposer d'un outil de supervision du réseau dès lors que celui-ci comporte un grand nombre d'hôtes qui inter-agissent, stations, serveurs, éléments de routage ou de commutation ou encore boites noires.

D'après la RFC 1213 (MIB II) le cadre de travail de SNMP repose sur trois composantes :



* SMI définit les types d'objets utilisés dans les mibs. C'est une sorte de méta modèle de données. Par exemple pour définir une adresse physique (MAC)

  ​

```
    PhysAddress ::=
         OCTET STRING
    -- This data type is used to model media addresses.  For many
    -- types of media, this will be in a binary representation.
    -- For example, an ethernet address would be represented as
    -- a string of 6 octets.
```



* La MIB décrit une collection structurée des ressources à gérer. Une ressource à gérer est représentée par un objet.

  ​

```sn
-- the TCP Connection table

            -- The TCP connection table contains information about this
            -- entity's existing TCP connections.

            tcpConnTable OBJECT-TYPE
                SYNTAX  SEQUENCE OF TcpConnEntry
                ACCESS  not-accessible
                STATUS  mandatory
                DESCRIPTION
                        "A table containing TCP connection-specific
                        information."
                ::= { tcp 13 }

            tcpConnEntry OBJECT-TYPE
                SYNTAX  TcpConnEntry
                ACCESS  not-accessible
                STATUS  mandatory
                DESCRIPTION
                        "Information about a particular current TCP
                        connection.  An object of this type is transient,
                        in that it ceases to exist when (or soon after)
                        the connection makes the transition to the CLOSED
                        state."
                INDEX   { tcpConnLocalAddress,
                          tcpConnLocalPort,
                          tcpConnRemAddress,
                          tcpConnRemPort }
                ::= { tcpConnTable 1 }

            TcpConnEntry ::=
                SEQUENCE {
                    tcpConnState
                        INTEGER,
                    tcpConnLocalAddress
                        IpAddress,
                    tcpConnLocalPort
                        INTEGER (0..65535),
                    tcpConnRemAddress
                        IpAddress,
                    tcpConnRemPort
                        INTEGER (0..65535)
                }
```



* Le protocole SNMP qui régit le contenu des dialogues clients/serveurs c'est à dire l'interrogation des données structurées par la MIB.	

  ​

#### NETCONF / YANG

##### [NETCONF](http://www.bortzmeyer.org/6241.html)

   NETCONF est un protocole de gestion de la configuration des dispositifs de données en réseau. Il est conçu pour couvrir les insuffisances de « Simple Network Management Protocol » (SNMP) et Command-Line Interface (CLI), dans les fonctions de configurations réseaux. Le protocole prévoit des mécanismes d’installation, manipulation, et suppression de la configuration des périphériques réseaux. Il utilise un langage de balisage extensible (XML) codant les données de configuration ainsi que les messages du protocole.
     Le protocole NETCONF utilise un appel de procédure distante (RPC). Un client encode un RPC en XML et l'envoie à un serveur utilisant une méthode de connexion sécurisée. Le serveur répond avec une réponse codée au format XML.

**De SNMP**, il retient, entre autres, le modèle de données arborescent et hiérarchique qui permet de classifier les données de gestion de réseaux par catégories et sous-catégories : interfaces réseaux, routage, système, etc. 

**De CLI**, il retient l’approche externalisée du modèle de sécurité (SSH) et le côté plus orienté configuration que monitoring. NETCONF dispose à la fois d’une configuration running, c’est-à-dire en cours de production, d’une configuration startup lancée au démarrage de la machine, et d’une nouveauté, une configuration candidate qui permet de travailler sur une configuration off-line et de la valider avant de la mettre en production. 

Le côté transactionnel de Netconf, avec cette configuration candidate, les mécanismes de validation avant la mise en production et les verrous qui garantissent un accès en isolation accroissent la sureté de configuration. Netconf a l’avantage de pouvoir valider une configuration par rapport à sa syntaxe et sa structure. En effet, si le modèle de données est décrit avec des schémas XML ou des DTD, il est possible lors d’une opération copy-config de vérifier que sa structure est correcte. Cette vérification est également valable pour les messages reçus, ce qui permet de traiter plus facilement les cas d’erreurs et évite de commencer à traiter le message s’il n’est pas valide par rapport au schéma XML de Netconf. 

##### YANG

Netconf est un standard IETF (RFC 6241) visant à standardiser les directives réseau auprès des équipements. YANG est un langage permettant la modélisation des services réseau. 

Une directive Netconf pourra contenir un modèle YANG et ainsi configurer de la même manière des équipements de constructeurs différents, si tant est qu’ils implémentent bien le service demandé et cette API de configuration. 


Yang a donc bien des points communs avec le **SMI** des [RFC 2578](http://www.bortzmeyer.org/2578.html) et [RFC 2579](https://www.rfc-editor.org/rfc/rfc2579.txt). Avant **Netconf**, beaucoup de gens pensaient que toute la gestion des équipements réseau se ferait en **SNMP**, en s'appuyant sur ce modèle SMI. Si, pour la lecture des variables, SNMP s'est largement imposé, force est de constater que, pour l'écriture de variables et pour les actions, SNMP reste très peu utilisé, au profit de toute une galaxie de mécanismes privés (Web, **REST**, **SSH** + **CLI**, etc), galaxie que Netconf vise à remplacer. Une **MIB** du SMI peut donc être traduite en Yang, l'inverse n'étant pas vrai (Yang étant plus riche).

La **syntaxe** de Yang utilise des groupes emboîtés, délimités par des **accolades**. Mais une syntaxe équivalente, en **XML**, existe, sous le nom de Yin. Tout module Yang peut être traduit en Yin sans perte et réciproquement (voir la section 11 pour plus de détails sur Yin).

Donc, un engin donné, **routeur** ou autre équipement qu'on veut gérer, est décrit par des modules Yang. Lorsqu'un serveur Netconf à bord dudit engin met en œuvre un module Yang, cela veut dire qu'il permet de modifier, via Netconf, les variables décrites dans le module (le serveur typique met en œuvre plusieurs modules). Voici le début d'un module possible :

```
     // Only an example, not a real module. 
     module acme-system {
         namespace "http://acme.example.com/system";
         prefix "acme";

         organization "ACME Inc.";
         contact "joe@acme.example";
         description
             "The module for entities implementing the ACME system.";

         revision 2010-08-05 {
             description "Initial revision.";
         }
...
```

On l'a dit, Yang est arborescent. Les feuilles de l'arbre (section 4.2.2.1 du RFC) contiennent une valeur particulière, par exemple, ici, le nom de l'engin géré :

```
       leaf host-name {
           type string;
           description "Hostname for this system";
       }
```

Ici, `leaf` est un mot-clé de Yang qui indique une feuille de l'arbre (plus de nœuds en dessous), `host-name` est le nom que l'auteur du module a donné à une variable, de type « chaîne de caractères ». Lorsqu'un serveur Netconf enverra cette information à un client (ou réciproquement), elle sera encodée en **XML** ainsi (Netconf utilise XML pour l'encodage des messages) :

```
       <host-name>my-router.example.com</host-name>
```

Donc, pour résumer, Yang modélise ce qu'on **peut** lire ou modifier, Netconf permet de le lire ou de le modifier effectivement.

Par contre, si un nœud de l'arbre Yang n'est pas une feuille, il est désigné par le mot-clé `container`. Par exemple, il y a ici deux `containers` emboîtés et une feuille :

```
     container system {
         container login {
             leaf message {
                 type string;
                 description
                     "Message given at start of login session";
             }
         }
     }
```

Lorsque Netconf utilise cette donnée, cela ressemblera, sur le câble, à ceci :

```
     <system>
       <login>
         <message>Good morning</message>
       </login>
     </system>
```

Yang dispose d'un certain nombre de **types** pour représenter les données (section 4.2.4 et [RFC 6991](http://www.bortzmeyer.org/6991.html)), mais on peut aussi créer ses types (sections 4.2.5 et 7.3) par exemple ainsi :

```
     typedef percent {
         type uint8 {
             range "0 .. 100";
         }
         description "Percentage";
     }

     leaf completed {
         type percent;
     }
```

On a ajouté un intervalle de validité au type prédéfini `uint8`. Autre exemple, en indiquant une valeur par défaut, et en dérivant d'un type défini dans le module `inet` :

```
     typedef listen-ipv4-address {
         type inet:ipv4-address;
         default "0.0.0.0";
     }
```



#### [RESTCONF](http://www.bortzmeyer.org/8040.html)

Pour configurer à distance un équipement réseau (par exemple un **routeur** ou bien un **commutateur**), il existait déjà le protocole **NETCONF** ([RFC 6241](http://www.bortzmeyer.org/6241.html)). Fondé sur un échange de données en **XML**, il n'a pas convaincu tout le monde, qui aurait préféré un protocole **REST**. C'est désormais fait avec RESTCONF, décrit dans ce RFC.

RESTCONF est donc bâti sur **HTTP** ([RFC 7230](http://www.bortzmeyer.org/7230.html)) et les opérations **CRUD**. Comme NETCONF, RESTCONF utilise des modèles de données décrits en **YANG** ([RFC 7950](http://www.bortzmeyer.org/7950.html)). Il devrait donc permettre de configurer plus simplement les équipements réseau. (Les historiens noteront que l'ancêtre **SNMP** avait été prévu, non seulement pour **lire** des informations, mais également pour **écrire**, par exemple pour modifier la configuration d'un routeur. Cette possibilité n'a eu aucun succès. Cet échec est une des raisons pour lesquelles NETCONF a été développé.)

Les opérations **CRUD** sont donc faites avec les méthodes classiques de **HTTP** ([RFC 7231](http://www.bortzmeyer.org/7231.html)). Lire l'état de l'engin se fait évidemment avec la méthode `GET`. Le modifier se fait avec une des méthodes parmi `PUT`, `DELETE`, `POST` ou `PATCH` (cf. section 4 du RFC). Les données envoyées, ou bien lues, sont encodées, au choix, en **XML** ou en **JSON**. À noter que RESTCONF, conçu pour les cas relativement simples, est plus limité que NETCONF (il n'a pas de fonction de **verrou**, par exemple). Il ne peut donc pas complètement remplacer NETCONF (ainsi, si un client NETCONF a mis un verrou sur une ressource, le client RESTCONF ne peut pas y accéder, voir la section 1.4 du RFC). Mais le RFC fait quand même plus de 130 pages, avec plein d'options.

## OpenConfig

L'[IETF](https://www.ietf.org/archive/id/draft-openconfig-netmod-model-catalog-01.txt) et [Openconfig](http://www.openconfig.net/) veulent résoudre ces deux défis :

- des constructeurs **différents** ont des commandes / syntaxes CLI **différentes**

- des constructeurs **différents** restituent des données identiques dans des formats **différents**

  ​

**OpenConfig vise à modéliser (en YANG) des fonctions réseau (configuration et télémétrie), de façon neutre et indépendante des constructeurs/éditeurs.** 



OpenConfig est supporté par des [constructeurs majeurs](http://www.openconfig.net/about/participants/) ([Arista](https://eos.arista.com/openconfig-the-emerging-industry-standard-api-for-network-elements/), [Cisco ](https://newsroom.cisco.com/press-release-content?articleId=1727796), [Juniper](http://forums.juniper.net/t5/Automation-Programmability/Network-Programmability-with-OpenConfig-and-Junos/ba-p/289136)), des grandes entreprises (Google, Microsoft, Facebook, etc) ou des grands opérateurs télécoms (AT&T, British Telecom, Level 3, etc).

Exemple de modèles de données fournis par OpenConfig :

![](https://raw.githubusercontent.com/jmanteau/lprims-netautomation/master/openconfig-models.svg?sanitize=true)



**OpenConfig Exemple**

extrait de modèle YANG OpenConfig pour BGP

```
  typedef peer-type {
    type enumeration {
      enum INTERNAL {
        description "internal (iBGP) peer";
      }
      enum EXTERNAL {
        description "external (eBGP) peer";
      }
    }
    description
      "labels a peer or peer group as explicitly internal or
      external";
  }
```

Remplissage du modèle:

```
>>> from oc_bgp import bgp 

>>> oc = bgp()

>>> oc.bgp.global_.config.as_ = 2856

>>> oc.bgp.global_.config.router_id = "10.152.0.4"

>>> oc.bgp.neighbors.neighbor.add("192.168.1.2")

>>> oc.bgp.neighbors.neighbor["192.168.1.2"].config.peer_as = 5400

>>> oc.bgp.neighbors.neighbor["192.168.1.2"].config.description = "a fictional transit session" 
```

Résultat en JSON:

```json
{
    "bgp": {
        "neighbors": {
            "neighbor": {
                "192.168.1.2": {
                    "neighbor-address": "192.168.1.2", 
                    "config": {
                        "peer-type": "EXTERNAL", 
                        "peer-as": 5400, 
                        "description": "a fictional transit session"
                    }
                }
            }
        }, 
        "global": {
            "config": {
                "as": 2856, 
                "router-id": "10.152.0.4"
            }
        }
    }
}
```



## Vision simplifiée du modèle d'administration réseau 

![](https://github.com/jmanteau/lprims-netautomation/raw/master/networkadminstack.png)



## Outils d'automatisation des réseaux

### Versionning (Git)

Git est en dehors du scope de ce cours. Il est cependant nécessaire de maitriser Git aujourd'hui en tant qu'ingénieur réseau. Que cela soit pour sauvegarder les configurations, partager du code ou des templates de configuration sur un repository central.

Les deux liens suivants sont une bonne introduction à cet outil:

https://try.github.io/

https://www.atlassian.com/git

### Templating (Jinja)

### Extracting Information

Regex

TextFSM

Fact Gathering

NTC Napalm

### Ansible

### Napalm





# TP

## Setup

[GNS3 VM](https://docs.gns3.com/1wdfvS-OlFfOf7HWZoSXMbG58C4pMSy7vKJFiKKVResc/index.html)

[GNS3 Client](https://docs.gns3.com/)

[Ansible](http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installation-guide)

## Consignes

![](https://github.com/jmanteau/lprims-netautomation/raw/master/TP%20IUT%20Network%20Automation.png)

### Facts

[Vyos Facts](http://docs.ansible.com/ansible/latest/modules/vyos_facts_module.html#vyos-facts-module)

[IOS facts](http://docs.ansible.com/ansible/latest/modules/ios_facts_module.html#ios-facts-module)

### System

[Vyos System](http://docs.ansible.com/ansible/latest/modules/vyos_system_module.html#vyos-system-module)

[IOS System](http://docs.ansible.com/ansible/latest/modules/ios_system_module.html#ios-system-module)

###Interfaces

[Vyos Interface L3](http://docs.ansible.com/ansible/latest/modules/vyos_l3_interface_module.html#vyos-l3-interface-module)

[IOS Interface L3](http://docs.ansible.com/ansible/latest/modules/ios_l3_interface_module.html#ios-l3-interface-module)

### BGP

[IOS Config](http://docs.ansible.com/ansible/latest/modules/ios_config_module.html)

[Vyos Config](http://docs.ansible.com/ansible/latest/modules/vyos_config_module.html#vyos-config-module)



## Résultat attendu

Playbook qui sera joué from scratch

# References

[Network Programmability and Automation](https://www.amazon.fr/Network-Programmability-Automation-Jason-Edelman/dp/1491931256/)

https://github.com/ipspace/ansible-examples

[DevNet Workshop- NetDevOps for the Network Dude - How to get started with APIs, Ansible and Python](https://clnv.s3.amazonaws.com/2018/eur/pdf/DEVNET-1002.pdf)

[Introduction to Catalyst Programmability](https://clnv.s3.amazonaws.com/2018/eur/pdf/BRKCRS-1450.pdf)

[DevNet Workshop- Hands-On Kicking the Tires of RESTCONF](https://clnv.s3.amazonaws.com/2018/eur/pdf/DEVNET-2585.pdf)

[DevNet Workshop- Hands On Exploration of NETCONF and YANG](https://clnv.s3.amazonaws.com/2018/eur/pdf/DEVNET-2561.pdf)

[SDx Open Source in Networking Report](https://www.sdxcentral.com/reports/2017/open-source-networking/) 

[Training Course for Ansible Network Automation](https://github.com/network-automation/linklight)

[Structurer vos données avec XML](https://openclassrooms.com/courses/structurez-vos-donnees-avec-xml)