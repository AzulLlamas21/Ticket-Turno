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

 Date: 11/07/2024 23:21:04
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
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of asunto
-- ----------------------------
INSERT INTO `asunto` VALUES (1, 'Ingreso');
INSERT INTO `asunto` VALUES (2, 'Egreso');
INSERT INTO `asunto` VALUES (3, 'Pago de Inscripción');
INSERT INTO `asunto` VALUES (4, 'Selección de Horario');
INSERT INTO `asunto` VALUES (5, 'Recoger papelería');

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
  `telefono` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `celular` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `correo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `id_nivel` int(11) NULL DEFAULT NULL,
  `id_mun` int(11) NOT NULL,
  `id_asunto` int(11) NULL DEFAULT NULL,
  `estado` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_mun`, `no_turno`) USING BTREE,
  INDEX `id_nivel`(`id_nivel`) USING BTREE,
  INDEX `id_asunto`(`id_asunto`) USING BTREE,
  CONSTRAINT `formulario_ibfk_1` FOREIGN KEY (`id_nivel`) REFERENCES `nivel` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `formulario_ibfk_2` FOREIGN KEY (`id_mun`) REFERENCES `municipio` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `formulario_ibfk_3` FOREIGN KEY (`id_asunto`) REFERENCES `asunto` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of formulario
-- ----------------------------
INSERT INTO `formulario` VALUES (1, 'ZYXW987654MNOPQRT0', 'Maria', 'Garcia', 'Martinez', '1112223334', '4445556667', 'maria.garcia@example.com', 2, 1, 2, 'Activo');
INSERT INTO `formulario` VALUES (3, 'KXXX987654MNOPQRT0', 'Tinkiwinky', 'Lala', 'Po', '2212243334', '5566556667', 'Tinky@example.com', 9, 1, 3, 'Activo');
INSERT INTO `formulario` VALUES (4, 'AEAX010101MNEXXXR5', 'José', 'Alcala', 'Alvarez', '5551234587', '5559876583', 'lualvares@example.com', 1, 1, 3, 'Resuelto');
INSERT INTO `formulario` VALUES (5, 'AEAX010101MNEXXXR5', 'Jose', 'Pérez', 'García', '5551234587', '5559876583', 'jose.perez@example.com', 1, 1, 1, 'Pendiente');
INSERT INTO `formulario` VALUES (6, 'LATA011228MCMISIR2', 'Rafael', 'Gomez', 'Palacios', '0987654321', '1234567890', 'rr@example.com', 9, 1, 2, 'Resuelto');
INSERT INTO `formulario` VALUES (7, 'JJAA010101MNEXXXR5', 'Jose', 'Alcala', 'Alvares', '5551234587', '5559876583', 'jalvares@example.com', 1, 1, 1, 'Pendiente');
INSERT INTO `formulario` VALUES (8, 'LJAA010101MNEXXXR5', 'Luis', 'Alcala', 'Alvares', '5551234587', '5559876583', 'lualvares@example.com', 6, 1, 5, 'Pendiente');
INSERT INTO `formulario` VALUES (1, 'ABCD123456HDFRRT01', 'Juan', 'Perez', 'Lopez', '1234567890', '0987654321', 'juan.perez@example.com', 1, 2, 1, 'activo');
INSERT INTO `formulario` VALUES (2, 'KXXX987654MNOPQRT0', 'Tinkiwinky', 'Lala', 'Po', '2212243334', '5566556667', 'Tinky@example.com', 9, 2, 3, 'Resuelto');

-- ----------------------------
-- Table structure for municipio
-- ----------------------------
DROP TABLE IF EXISTS `municipio`;
CREATE TABLE `municipio`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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

-- ----------------------------
-- Table structure for nivel
-- ----------------------------
DROP TABLE IF EXISTS `nivel`;
CREATE TABLE `nivel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nivel` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
-- Records of usuarios
-- ----------------------------
INSERT INTO `usuarios` VALUES (1, 'azul', 'azul');
INSERT INTO `usuarios` VALUES (2, 'admin', 'admin');
INSERT INTO `usuarios` VALUES (3, 'otroadmin', 'otroadmin');

SET FOREIGN_KEY_CHECKS = 1;
