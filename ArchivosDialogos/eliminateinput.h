#ifndef ELIMINATEINPUT_H
#define ELIMINATEINPUT_H

#include <QDialog>

namespace Ui {
class EliminateInput;
}

class EliminateInput : public QDialog
{
    Q_OBJECT

public:
    explicit EliminateInput(QWidget *parent = nullptr);
    ~EliminateInput();

private:
    Ui::EliminateInput *ui;
};

#endif // ELIMINATEINPUT_H
