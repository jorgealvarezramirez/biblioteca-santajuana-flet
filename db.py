# db.py
import sqlite3

def conectar():
    conn = sqlite3.connect("biblioteca.db")
    return conn

def crear_tabla_libros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            anio INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertar_libro(titulo, autor, anio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", (titulo, autor, anio))
    conn.commit()
    conn.close()

def obtener_libros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conn.close()
    return libros

def eliminar_libro(id_libro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    conn.close()


#------------------------------------------------


def crear_tabla_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertar_usuario(nombre, tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, tipo) VALUES (?, ?)", (nombre, tipo))
    conn.commit()
    conn.close()

def obtener_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def eliminar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()
    conn.close()

def crear_tabla_prestamos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            id_libro INTEGER,
            fecha TEXT DEFAULT CURRENT_DATE,
            devuelto INTEGER DEFAULT 0,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
            FOREIGN KEY (id_libro) REFERENCES libros(id)
        )
    """)
    conn.commit()
    conn.close()

def insertar_prestamo(id_usuario, id_libro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prestamos (id_usuario, id_libro) VALUES (?, ?)", (id_usuario, id_libro))
    conn.commit()
    conn.close()

def obtener_prestamos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, u.nombre, l.titulo, p.fecha, p.devuelto
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id
        JOIN libros l ON p.id_libro = l.id
        ORDER BY p.fecha DESC
    """)
    prestamos = cursor.fetchall()
    conn.close()
    return prestamos

def devolver_prestamo(id_prestamo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE prestamos SET devuelto = 1 WHERE id = ?", (id_prestamo,))
    conn.commit()
    conn.close()

def obtener_libros_disponibles():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM libros
        WHERE id NOT IN (
            SELECT id_libro FROM prestamos WHERE devuelto = 0
        )
    """)
    disponibles = cursor.fetchall()
    conn.close()
    return disponibles

