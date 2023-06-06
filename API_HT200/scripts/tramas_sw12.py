fases_frame = bytearray(13)
fases_frame[0] =192
fases_frame[1] =16
fases_frame[2] =32
fases_frame[3] =16
fases_frame[4] =3
fases_frame[5] =1
fases_frame[6] =1
fases_frame[7] =0
fases_frame[8] =128
fases_frame[9] =7
fases_frame[10] =0
fases_frame[11] =204
fases_frame[12] =192

#planes frame

plan1_frame = bytearray(14)
plan1_frame[0] =192
plan1_frame[1] =16
plan1_frame[2] =32
plan1_frame[3] =16
plan1_frame[4] =3
plan1_frame[5] =1
plan1_frame[6] =1
plan1_frame[7] =0
plan1_frame[8] =128
plan1_frame[9] =8
plan1_frame[10] =1
plan1_frame[11] =0
plan1_frame[12] =206
plan1_frame[13] =192

plan2_frame = bytearray(14)
plan2_frame[0] =192
plan2_frame[1] =16
plan2_frame[2] =32
plan2_frame[3] =16
plan2_frame[4] =3
plan2_frame[5] =1
plan2_frame[6] =1
plan2_frame[7] =0
plan2_frame[8] =128
plan2_frame[9] =8
plan2_frame[10] =1
plan2_frame[11] =1
plan2_frame[12] =207
plan2_frame[13] =192

plan3_frame = bytearray(14)
plan3_frame[0] =192
plan3_frame[1] =16
plan3_frame[2] =32
plan3_frame[3] =16
plan3_frame[4] =3
plan3_frame[5] =1
plan3_frame[6] =1
plan3_frame[7] =0
plan3_frame[8] =128
plan3_frame[9] =8
plan3_frame[10] =1
plan3_frame[11] =2
plan3_frame[12] =208
plan3_frame[13] =192

plan4_frame = bytearray(14)
plan4_frame[0] =192
plan4_frame[1] =16
plan4_frame[2] =32
plan4_frame[3] =16
plan4_frame[4] =3
plan4_frame[5] =1
plan4_frame[6] =1
plan4_frame[7] =0
plan4_frame[8] =128
plan4_frame[9] =8
plan4_frame[10] =1
plan4_frame[11] =3
plan4_frame[12] =209
plan4_frame[13] =192

plan5_frame = bytearray(14)
plan5_frame[0] =192
plan5_frame[1] =16
plan5_frame[2] =32
plan5_frame[3] =16
plan5_frame[4] =3
plan5_frame[5] =1
plan5_frame[6] =1
plan5_frame[7] =0
plan5_frame[8] =128
plan5_frame[9] =8
plan5_frame[10] =1
plan5_frame[11] =4
plan5_frame[12] =210
plan5_frame[13] =192

plan6_frame = bytearray(14)
plan6_frame[0] =192
plan6_frame[1] =16
plan6_frame[2] =32
plan6_frame[3] =16
plan6_frame[4] =3
plan6_frame[5] =1
plan6_frame[6] =1
plan6_frame[7] =0
plan6_frame[8] =128
plan6_frame[9] =8
plan6_frame[10] =1
plan6_frame[11] =5
plan6_frame[12] =211
plan6_frame[13] =192

plan7_frame = bytearray(14)
plan7_frame[0] =192
plan7_frame[1] =16
plan7_frame[2] =32
plan7_frame[3] =16
plan7_frame[4] =3
plan7_frame[5] =1
plan7_frame[6] =1
plan7_frame[7] =0
plan7_frame[8] =128
plan7_frame[9] =8
plan7_frame[10] =1
plan7_frame[11] =6
plan7_frame[12] =212
plan7_frame[13] =192

plan8_frame = bytearray(14)
plan8_frame[0] =192
plan8_frame[1] =16
plan8_frame[2] =32
plan8_frame[3] =16
plan8_frame[4] =3
plan8_frame[5] =1
plan8_frame[6] =1
plan8_frame[7] =0
plan8_frame[8] =128
plan8_frame[9] =8
plan8_frame[10] =1
plan8_frame[11] =7
plan8_frame[12] =213
plan8_frame[13] =192

#tramas de tiempo
#ordinario
horarios_frame = bytearray(14)
horarios_frame[0] =192
horarios_frame[1] =16
horarios_frame[2] =32
horarios_frame[3] =16
horarios_frame[4] =3
horarios_frame[5] =1
horarios_frame[6] =1
horarios_frame[7] =0
horarios_frame[8] =128
horarios_frame[9] =9
horarios_frame[10] =1
horarios_frame[11] =0
horarios_frame[12] =207
horarios_frame[13] =192





#fin de semana
semana_frame = bytearray(14)
semana_frame[0] =192
semana_frame[1] =16
semana_frame[2] =32
semana_frame[3] =16
semana_frame[4] =3
semana_frame[5] =1
semana_frame[6] =1
semana_frame[7] =0
semana_frame[8] =128
semana_frame[9] =9
semana_frame[10] =1
semana_frame[11] =1
semana_frame[12] =208
semana_frame[13] =192



#festivo
festivo_frame = bytearray(14)
festivo_frame[0] =192
festivo_frame[1] =16
festivo_frame[2] =32
festivo_frame[3] =16
festivo_frame[4] =3
festivo_frame[5] =1
festivo_frame[6] =1
festivo_frame[7] =0
festivo_frame[8] =128
festivo_frame[9] =9
festivo_frame[10] =1
festivo_frame[11] =2
festivo_frame[12] =209
festivo_frame[13] =192

#tramas de grupo
grupos_frame = bytearray(14)
grupos_frame[0] =192
grupos_frame[1] =16
grupos_frame[2] =32
grupos_frame[3] =16
grupos_frame[4] =3
grupos_frame[5] =1
grupos_frame[6] =1
grupos_frame[7] =0
grupos_frame[8] =128
grupos_frame[9] =6
grupos_frame[10] =0
grupos_frame[11] =203
grupos_frame[12] =192


#trama conflictos de verdes

grenn_conflict = bytearray(14)
grenn_conflict[0] =192
grenn_conflict[1] =16
grenn_conflict[2] =32
grenn_conflict[3] =16
grenn_conflict[4] =3
grenn_conflict[5] =1
grenn_conflict[6] =1
grenn_conflict[7] =0
grenn_conflict[8] =128
grenn_conflict[9] =17
grenn_conflict[10] =0
grenn_conflict[11] =214
grenn_conflict[12] =192


#trama de parametros operativos
operative_frame = bytearray(14)
operative_frame[0] =192
operative_frame[1] =16
operative_frame[2] =32
operative_frame[3] =16
operative_frame[4] =3
operative_frame[5] =1
operative_frame[6] =1
operative_frame[7] =0
operative_frame[8] =128
operative_frame[9] =8
operative_frame[10] =1
operative_frame[11] =16
operative_frame[12] =222
operative_frame[13] =192

#trama tiempo del controlador
time_frame = bytearray(14)
time_frame[0] =192
time_frame[1] =16
time_frame[2] =32
time_frame[3] =16
time_frame[4] =3
time_frame[5] =1
time_frame[6] =1
time_frame[7] =0
time_frame[8] =128
time_frame[9] =5
time_frame[10] =0
time_frame[11] =202
time_frame[12] =192

#especial frame

especial_frame = bytearray(14)
especial_frame[0] =192
especial_frame[1] =16
especial_frame[2] =32
especial_frame[3] =16
especial_frame[4] =3
especial_frame[5] =1
especial_frame[6] =1
especial_frame[7] =0
especial_frame[8] =128
especial_frame[9] =9
especial_frame[10] =1
especial_frame[11] =3
especial_frame[12] =210
especial_frame[13] =192

#entradas frame

entradas_frame = bytearray(14)
entradas_frame[0] =192
entradas_frame[1] =16
entradas_frame[2] =32
entradas_frame[3] =16
entradas_frame[4] =3
entradas_frame[5] =1
entradas_frame[6] =1
entradas_frame[7] =0
entradas_frame[8] =128
entradas_frame[9] =16
entradas_frame[10] =1
entradas_frame[11] =0
entradas_frame[12] =214
entradas_frame[13] =192

#errores frame

errores_frame = bytearray(14)
errores_frame[0] =192
errores_frame[1] =16
errores_frame[2] =32
errores_frame[3] =16
errores_frame[4] =3
errores_frame[5] =1
errores_frame[6] =1
errores_frame[7] =0
errores_frame[8] =128
errores_frame[9] =11
errores_frame[10] =1
errores_frame[11] =255
errores_frame[12] =208
errores_frame[13] =192












