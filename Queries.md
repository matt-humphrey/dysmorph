# Queries

- How does the coding for dysmorphologies change?
    - It appears different (at least for eyes) between G200 and G201 - don't harmonise?
- How to harmonise when some dysmorphology questions have multiple variables and others are concatenated?

## Issues

### Differing value labels

Ex. for eyes:

G200:
-99="Missing";0="NIL";1="Ptosis";2="Abnormal palpebral fissures";3="Hypertelorism";4="Epicanthic folds";5="Blepharophimosis";6="Telecanthus";7="Abnormal irides";8="Epibulbar dermoids";9="Long lashes";10="Absent lashes";11="Eyebrows- inner missing";12="Eyebrows- outer missing";13="Synophyris (eyebrows meet)";97="Other"

G201:
-99="Missing";-88="N/A";1="Convergent strabismus-manifest";2="Convergent strabismus-latent(cover test only)";3="Divergent strabismus-manifest";4="Divergent strabismus-latent";5="Unequal pupils";6="Non-reactive pupils";7="Other pupillary abnormalities";8="Corneal opacity";9="Cateract or other lens opacity";10="Lens dislocation";11="Retinal pigmentation";12="Abnormal irides";13="Other colobomata";14="Microphthalmos";15="Short palpebral fissures";16="Upslanting palpebral fissures(mongoloid slant)";17="Downslanting palpebral fissures(anti mongoloid slant)";18="Hypertelorism";19="Hypotelorism";20="Epicanthic folds";21="Ptosis";22="Abnormal eyebrows";23="Conjuctivitis";24="Tearing";25="Conjunctivce haemorrhage";26="Other"

G202:
-99="Missing";-88="N/A";1="Convergent strabismus-manifest";2="Convergent strabismus-latent(cover test only)";3="Divergent strabismus-manifest";4="Divergent strabismus-latent";5="Unequal pupils";6="Non-reactive pupils";7="Other pupillary abnormalities";8="Corneal opacity";9="Cateract or other lens opacity";10="Lens dislocation";11="Retinal pigmentation";12="Abnormal irides";13="Other colobomata";14="Microphthalmos";15="Short palpebral fissures";16="Upslanting palpebral fissures(mongoloid slant)";17="Downslanting palpebral fissures(anti mongoloid slant)";18="Hypertelorism";19="Hypotelorism";20="Epicanthic folds";21="Ptosis";22="Abnormal eyebrows";23="Conjuctivitis";24="Tearing";25="Conjunctivce haemorrhage";26="Other"

G203:
-99="Missing";-88="N/A";1="Convergent strabismus-manifest";2="Convergent strabismus-latent(cover test only)";3="Divergent strabismus-manifest";4="Divergent strabismus-latent";5="Unequal pupils";6="Non-reactive pupils";7="Other pupillary abnormalities";8="Corneal opacity";9="Cateract or other lens opacity";10="Lens dislocation";11="Retinal pigmentation";12="Abnormal irides";13="Other colobomata";14="Microphthalmos";15="Short palpebral fissures";16="Upslanting palpebral fissures(mongoloid slant)";17="Downslanting palpebral fissures(anti mongoloid slant)";18="Hypertelorism";19="Hypotelorism";20="Epicanthic folds";21="Ptosis";22="Abnormal eyebrows";23="Conjuctivitis";24="Tearing";25="Conjunctivce haemorrhage";26="Other"

G205:
-88="N/A";-99="Missing";A="A = convergent strabismus - manifest";AZ="A and Z";B="B = convergent strabismus - latent";C="C = divergent strabismus - manifest";CZ="C and Z";D="D = divergent strabismus - latent";E="E = unequal pupils";F="F = non-reactive pupil(s)";G="G = other pupillary abnormalities";H="H = corneal opacity";I="I = cataract(s) or other lens opacity";J="J = lens dislocation";K="K = retinal pigmentation";L="L = abnormal irides";M="M = other colobamata";N="N = microphthalmos";O="O = short palpebral fissures";P="P = upslanting palpebral fissures (mongoloid slant)";PM="P and M";Q="Q = downslanting palpebral fissures (anti-mongoloid slant)";R="R = hypertelorism";S="S = hypotelorism";T="T = epicanthic eyefolds";U="U = ptosis";V="V = abnormal eyebrows";W="W = conjuntivitis";X="X = tearing";Y="Y = conjuntival haemorrhage";Z="Z = other";ZC="Z and C";ZE="Z and E"

G208:
-88="N/A";0="No dysmorphology recorded";1="Convergent strabismus - manifest";2="Unequal pupils";3="Upslanting palpebral fissures (mongoloid slant)";4="Conjuntivitis";5="Other"

---

Ears:

G200:
-99="Missing";0="NIL";1="Low set";2="Rotated";3="Pre-auricular tags";4="Creased lobes";5="Post-auricular tags";6="Abnormal helix";7="Abnormal tragus";8="Pits";9="Primitive shape";10="Fistulae";11="Asymmetry";12="Satyr (pointed)";97="Other"

G201:
-99="Missing";-88="N/A";1="Lowest ears";2="Rotated ears";3="Pre-auricular tags/pits";4="Malformed auricles";5="Small ears";6="Upward take-off of lobe";7="Retraction of tympanic membrane";8="Middle ear infection";9="Inflammation of tympanic membrane";10="Scarring of tympanic membrane";11="Prominent/bat ears";12="Grommets (tympanastomy tubes) in situ";13="Creased lobes";14="Abnormal helix";26="Tympanosclerosis"

-99="Missing";-88="N/A";1="Lowest ears";2="Rotated ears";3="Pre-auricular tags/pits";4="Malformed auricles";5="Small ears";6="Upward take-off of lobe";7="Retraction of tympanic membrane";8="Middle ear infection";9="Inflammation of tympanic membrane";10="Scarring of tympanic membrane";11="Prominent/bat ears";12="Grommets (tympanastomy tubes) in situ";13="Creased lobes";14="Abnormal helix";26="Tympanosclerosis"

-99="Missing";-88="N/A";1="Lowest ears";2="Rotated ears";3="Pre-auricular tags/pits";4="Malformed auricles";5="Small ears";6="Upward take-off of lobe";7="Retraction of tympanic membrane";8="Middle ear infection";9="Inflammation of tympanic membrane";10="Scarring of tympanic membrane";11="Prominent/bat ears";12="Grommets (tympanastomy tubes) in situ";13="Creased lobes";14="Abnormal helix";26="Tympanosclerosis"

G205:
-88="N/A";-99="Missing";A="A = lowset ears";B="B = rotated ears";C="C = pre-auricular tags/pits";CJ="C and J";CZ="C and Z";D="D = malformed auricles";E="E = small ears";F="F = upward take-off of lobe";G="G = retraction of tympanic membrane(s)";GIZ="G, i and Z";H="H = middle ear effusion";HI="H and I";HL="H and l";HZ="H and Z";I="I = inflammation of tympanic membrane(s)";IH="I and H";IZ="I and H";J="J = scarring of tympanic membrane(s)";K="K = prominent/bat ears";L="L = grommets (tympanostomy tubes) in situ";LH="L and H";LJ="L and J";LK="L and K";LZ="L and Z";LZE="L, Z and E";LZI="L, Z and I";M="M = creased lobes";O="O = abnormal helix";Z="Z = other";ZG="Z and G";ZI="Z and I";ZK="Z and K"

G208:
-88="N/A";0="No dysmorphology recorded"

**Notes**
- N was skipped, and so O should be converted to 14 (not 15).
- Why is Tympan.. 26? Doesn't match Z = "other"
- Should be low-set ears, not lowest

