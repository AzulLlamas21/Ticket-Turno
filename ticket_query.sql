/*
 Navicat Premium Data Transfer

 Source Server         : VERANO WEB 2024
 Source Server Type    : MySQL
 Source Server Version : 100432
 Source Host           : localhost:3306
 Source Schema         : ticket

 Target Server Type    : MySQL
 Target Server Version : 100432
 File Encoding         : 65001

 Date: 16/07/2024 17:38:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for asunto
-- ----------------------------
DROP TABLE IF EXISTS `asunto`;
CREATE TABLE `asunto`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asunto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for municipio
-- ----------------------------
DROP TABLE IF EXISTS `municipio`;
CREATE TABLE `municipio`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nivel
-- ----------------------------
DROP TABLE IF EXISTS `nivel`;
CREATE TABLE `nivel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nivel` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for usuarios
-- ----------------------------
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios`  (
  `no_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `contrasena` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`no_usuario`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for formulario
-- ----------------------------
DROP TABLE IF EXISTS `formulario`;
CREATE TABLE `formulario`  (
  `no_turno` int(11) NOT NULL,
  `curp` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `paterno` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `materno` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `celular` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `correo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_nivel` int(11) NOT NULL,
  `id_mun` int(11) NOT NULL,
  `id_asunto` int(11) NOT NULL,
  `estado` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`no_turno`, `id_nivel`, `id_mun`, `id_asunto`) USING BTREE,
  INDEX `NivelFormulario`(`id_nivel`) USING BTREE,
  INDEX `MunFormulario`(`id_mun`) USING BTREE,
  INDEX `AsuntoFormulario`(`id_asunto`) USING BTREE,
  CONSTRAINT `AsuntoFormulario` FOREIGN KEY (`id_asunto`) REFERENCES `asunto` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `MunFormulario` FOREIGN KEY (`id_mun`) REFERENCES `municipio` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `NivelFormulario` FOREIGN KEY (`id_nivel`) REFERENCES `nivel` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of asunto
-- ----------------------------
INSERT INTO `asunto` VALUES (1, 'Ingreso');
INSERT INTO `asunto` VALUES (2, 'Egreso');
INSERT INTO `asunto` VALUES (3, 'Pago de Inscripción');
INSERT INTO `asunto` VALUES (4, 'Selección de Horario');
INSERT INTO `asunto` VALUES (5, 'Recoger papelería');
INSERT INTO `asunto` VALUES (6, 'Veranos');
INSERT INTO `asunto` VALUES (7, 'Diplomado');

-- ----------------------------
-- Records of municipio
-- ----------------------------
INSERT INTO `municipio` VALUES (1, 'Saltillo');
INSERT INTO `municipio` VALUES (2, 'Arteaga');
INSERT INTO `municipio` VALUES (3, 'Ramos Arizpe');
INSERT INTO `municipio` VALUES (4, 'Monclova');
INSERT INTO `municipio` VALUES (5, 'Torreón');
INSERT INTO `municipio` VALUES (6, 'Acuña');
INSERT INTO `municipio` VALUES (7, 'Ocampo');
INSERT INTO `municipio` VALUES (8, 'Piedras Negras');
INSERT INTO `municipio` VALUES (9, 'San Buenaventura');

-- ----------------------------
-- Records of nivel
-- ----------------------------
INSERT INTO `nivel` VALUES (1, '1');
INSERT INTO `nivel` VALUES (2, '2');
INSERT INTO `nivel` VALUES (3, '3');
INSERT INTO `nivel` VALUES (4, '4');
INSERT INTO `nivel` VALUES (5, '5');
INSERT INTO `nivel` VALUES (6, '6');
INSERT INTO `nivel` VALUES (7, '7');
INSERT INTO `nivel` VALUES (8, '8');
INSERT INTO `nivel` VALUES (9, '9');
INSERT INTO `nivel` VALUES (10, '10');
INSERT INTO `nivel` VALUES (11, '11');
INSERT INTO `nivel` VALUES (12, '12');

-- ----------------------------
-- Records of usuarios
-- ----------------------------
INSERT INTO `usuarios` VALUES (1, 'azul', 'azul');
INSERT INTO `usuarios` VALUES (2, 'admin', 'admin');
INSERT INTO `usuarios` VALUES (3, 'otroadmin', 'otroadmin');

-- ----------------------------
-- Records of formulario
-- ----------------------------
INSERT INTO `formulario` VALUES (1, 'ABCD123456HDFRRT01', 'Juan', 'Perez', 'Lopez', '1234567890', '0987654321', 'juan.perez@example.com', 1, 2, 1, 'Activo');
INSERT INTO `formulario` VALUES (1, 'LJAA010101MNEXXXR5', 'Luis', 'Alcala', 'Alvarez', '5551234587', '5559876583', 'lualvares@example.com', 1, 4, 3, 'Resuelto');
INSERT INTO `formulario` VALUES (1, 'ZYXW987654MNOPQRT0', 'Maria', 'Garcia', 'Martinez', '1112223334', '4445556667', 'maria.garcia@example.com', 2, 1, 2, 'Activo');
INSERT INTO `formulario` VALUES (1, 'LATA011228MCLLRZA2', 'Sue', 'Kim', 'X', '1111111111', '0987654321', 'a@gamil.com', 2, 3, 5, 'pendiente');
INSERT INTO `formulario` VALUES (2, 'JJAA010101MNEXXXR5', 'Jose', 'Alcala', 'Alvarez', '5551236765', '5559854323', 'jalvarez@example.com', 1, 1, 1, 'Pendiente');
INSERT INTO `formulario` VALUES (2, 'ABCD123456HDFRRT01', 'Juana', 'Perales', '', '8881234567', '8765432134', 'juanap@example.com', 1, 3, 1, 'Activo');
INSERT INTO `formulario` VALUES (2, 'KXXX987654MNOPQRT0', 'Tinkiwinky', 'Lala', 'Po', '2212243334', '5566556667', 'Tinky@example.com', 9, 2, 3, 'Resuelto');
INSERT INTO `formulario` VALUES (3, 'KXXX987654MNOPQRT0', 'Tinkiwinky', 'Lala', 'Po', '2212243334', '5566556667', 'Tinky@example.com', 9, 2, 7, 'Activo');
INSERT INTO `formulario` VALUES (4, 'JJAA010101MNEXXXR5', 'Jose', 'Alcala', 'Alvares', '5551236765', '5559854323', 'jalvares@example.com', 1, 1, 1, 'Pendiente');
INSERT INTO `formulario` VALUES (5, 'PPJE010101MNEXXXR5', 'Perla', 'Peña', 'Juarez', '0981342658', '0981256489', 'peña@example.com', 6, 1, 3, 'Pendiente');
INSERT INTO `formulario` VALUES (6, 'LATA011228MCMISIR2', 'Rafael', 'Gomez', 'Palacios', '0987654321', '1234567890', 'rr@example.com', 9, 2, 7, 'Resuelto');


SET FOREIGN_KEY_CHECKS = 1;
