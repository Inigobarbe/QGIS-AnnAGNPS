#ifndef COORDINATE_H
#define COORDINATE_H

#include <QDialog>

namespace Ui {
class Coordinate;
}

class Coordinate : public QDialog
{
    Q_OBJECT

public:
    explicit Coordinate(QWidget *parent = nullptr);
    ~Coordinate();

private:
    Ui::Coordinate *ui;
};

#endif // COORDINATE_H
