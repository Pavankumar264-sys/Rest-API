from flask import Flask,jsonify

todo=Flask('__name__')

students = [
    {
        'id':1,
        'student_name': 'std1',
        'age': 21,
        'usn': '1kg22cs080'
    },
    {
        'id':2,
        'student_name': 'std2',
        'age': 21,
        'usn': '1kg22cs081'
    },
    {
        'id':3,
        'student_name': 'std3',
        'age': 21,
        'usn': '1kg22cs082'

    }

]
@todo.route('/students-list')
def student_list():

    return jsonify(students)


@todo.route('/student/get/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404


if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )